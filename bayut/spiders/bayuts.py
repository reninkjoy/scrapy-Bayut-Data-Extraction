import scrapy


class BayutsSpider(scrapy.Spider):
    name = 'bayuts'
    allowed_domains = ['https://www.bayut.com/to-rent/property/dubai/']
    start_urls = ['http://https://www.bayut.com/to-rent/property/dubai//']

    def parse(self, response):
        pass
