#  Crawling using request package
## Crawling TOI Archive News
To crawl any site using request a deep analysis of the site is required.

### Analysis
Start URL: https://timesofindia.indiatimes.com/archive.cms

The inital crawling url contains a links for each month and in each month there are date for each day.
![](images/TOI/001_Initial_page.png)
![](images/TOI/002_TOI_Date.png)

If we analise the url and the Javascript the we can calculate the url for each day

![](images/TOI/003_JS.png) and ![](images/TOI/004_PAGE_URL.png)

by using
``` python 
pre_date = datetime(1899,12,30)
d =  floor((date - pre_date).total_seconds()/86400)
```
