import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import pandas as pd
from datetime import datetime as dt
import math


class CrawlerDaysNews():

    def __init__(self, url, no_of_process=2):
        self.url = url
        self.no_of_process = no_of_process

    def get_news_urls(self):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features="html.parser")
        links = soup.findAll('table')[1].findAll('a')
        news_urls = []
        for link in links:
            try:
                if 'articleshow' in link.attrs['href']:
                    news_urls.append(link.attrs['href'])
            except:
                pass
        self.news_urls = news_urls

    @staticmethod
    def get_article(link):
        try:
            print(link)
            news = {}
            news['link'] = link
            link = link. replace('articleshow', 'articleshowprint')
            r = requests.get(link)
            soup = BeautifulSoup(r.content, features="html.parser")
            news['title'] = soup.find('h1', {'class': 'heading1'}).text
            news['pubdate'] = soup.find(
                'div', {'class': 'time_cptn'}).text.split('|')[-1]
            news['article'] = soup.find(
                'div', {'class': 'article_content'}).text
            return news
        except:
            return {'link': None, 'title': None, 'pubdate': None, 'article': None}

    def clean_df(self):
        self.article.dropna(inplace=True)
        self.article.drop_duplicates(inplace=True)
        self.article['pubdate'] = pd.to_datetime(self.article['pubdate'])

    def start(self):
        self.get_news_urls()
        p = Pool(self.no_of_process)
        self.article = p.map(CrawlerDaysNews.get_article, self.news_urls)
        p.close()
        p.join()
        self.article = pd.DataFrame(self.article)
        self.clean_df()


def get_days_url(date):
    if type(date) != dt:
        print("date is not in datetime format")
        return None
    d2 = math.floor((date-dt(1899, 12, 30, 0, 0, 0)).total_seconds()/86400)
    url = f"https://timesofindia.indiatimes.com/{date.year}/{date.month}/{date.day}/archivelist/year-{date.year},month-{date.month},starttime-{d2}.cms"
    return url


if __name__ == "__main__":
    print("start", dt.now())
    df = pd.DataFrame(columns=['pubdate', 'title', 'article', 'link'])
    for i in range(31, 29, -1):
        print("Started date ", i, dt.now())
        d1 = dt(2022, 1, i, 0, 0, 0)
        url = get_days_url(d1)
        c = CrawlerDaysNews(url, 4)
        c.start()
        df = df.append(c.article)
        df.to_excel("data.xlsx")
    print("completed", dt.now())
