from gc import callbacks
import scrapy
from urllib.parse import urljoin

class HansindiaSpider(scrapy.Spider):
    name = 'hansindia'
    allowed_domains = ['thehansindia.com']
    start_urls = ['https://www.thehansindia.com/']

    def parse(self, response):
        for link in response.css('#mySidenav li:not(.megamenu) a::attr(href)'):
            if not link.get().startswith('/'):
                continue
            yield response.follow(link.get(), callback=self.parse_section)
            # yield response.follow(urljoin(HansindiaSpider.start_urls[0],link.get()), callback=self.parse_section)
            
    def parse_section(self,response):
        a = set(response.css("#listing_main_level_top a::attr(href)").getall())
        for link in list(a):
            yield {"link": link}
            
