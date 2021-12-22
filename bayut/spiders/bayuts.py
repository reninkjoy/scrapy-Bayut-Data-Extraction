import scrapy


class BayutsSpider(scrapy.Spider):
    name = 'bayuts'
    allowed_domains = ['https://www.bayut.com/to-rent/property/dubai/']
    start_urls = ['http://https://www.bayut.com/to-rent/property/dubai//']

    def parse(self, response):
        for link in response.css('div._4041eb80'):
            yied{"link":link.css('a._287661cb').attrib['href']}
            
            
        for link in response.css('a.b7880daf'):
            if link.css("a.b7880daf").attrib['title']=="Next":
                next_page=link.css('a.b7880daf').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse,dont_filter=True)
