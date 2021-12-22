import scrapy


class BayutsSpider(scrapy.Spider):
    name = 'bayuts'
    allowed_domains = ['https://www.bayut.com/to-rent/property/dubai/']
    start_urls = ['http://https://www.bayut.com/to-rent/property/dubai//']

    def parse(self, response):
        for link in response.css('div._4041eb80'):
            yied{link.css('a._287661cb').attrib['href']}
