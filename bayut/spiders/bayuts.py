iimport scrapy
from .items import Author

class DatasSpider(scrapy.Spider):
    name = 'bayuts'
    domain_name = ['bayut.com']
    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']
    
    def parse(self, response):

        for link in response.css('div._4041eb80'):
            pages = link.css('a._287661cb').attrib['href']
            yield response.follow(pages,callback=self.parse_data)

        for link in response.css('a.b7880daf'):
            if link.css("a.b7880daf").attrib['title']=="Next":
                next_page=link.css('a.b7880daf').attrib['href']

#       go to next pages
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse,dont_filter=True)

    def parse_data(self,response):
#       setting order load in to json
        author = Author()
        author["property_id"]=None
        author['purpose']=None
        author['type']=None
        author['added_on']=None
        author['furnishing']=None
        author['price']=None
        author["location"] = None
        author['bed_bath_size']=None
        author["permit_number"]=None
        author["agent_name"]=None
        author["image_url"]=None
        author["breadcrumbs"]=None
        author["amenities"]=None
        author['description']=None

# #      fetch data
        author['property_id']=response.xpath("//span[@aria-label='Reference']/text()").get()
        author['purpose']=response.xpath("//span[@aria-label='Purpose']/text()").get()
        author['type']=response.xpath("//span[@aria-label='Type']/text()").get()
        author['added_on']=response.xpath("//span[@aria-label='Reactivated date']/text()").get()
        author["furnishing"]=response.xpath("//span[@aria-label='Furnishing']/text()").get()
        price={"currency": None,"amount":None}
        price['currency']=response.xpath("//span[@aria-label='Currency']/text()").get()
        price['amount']=response.xpath("//span[@aria-label='Price']/text()").get()
        author['price']=price
        author['location']=response.xpath("//div[@aria-label='Property header']/text()").get()
        bed_bath_size={"bedrooms":None,"bathrooms":None,"size":None }
        bed_bath_size['bedrooms']=response.xpath("//span[@class='fc2d1086']/text()").get()
        bed_bath_size['bathrooms']=response.xpath("//span[@class='fc2d1086']/text()").getall()[1]
        bed_bath_size['size']=response.xpath("//span[@class='fc2d1086']//span/text()").get()
        author['bed_bath_size']=bed_bath_size
        author["permit_number"]=response.xpath("//div[@class='_74093213']//span/text()").getall()[-1]
        author["agent_name"]=response.xpath("//span[@class='_55e4cba0']/text()").get()
        author["image_url"]=response.xpath("//img[@src][@aria-label='Cover photo']/@src").get()
        author["breadcrumbs"]=">".join(response.xpath("//span[@class='_327a3afc']/text()").getall()[1:])
        author["amenities"]=response.xpath("//span[@class='_005a682a']/text()").extract()
        author["description"]=" ".join(response.xpath("//span[@class='_2a806e1e']/text()").getall())

        yield author
#

