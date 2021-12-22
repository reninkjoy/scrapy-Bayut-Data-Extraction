import scrapy


class BayutsSpider(scrapy.Spider):
    name = 'bayuts'
    allowed_domains = ['https://www.bayut.com/to-rent/property/dubai/']
    start_urls = ['http://https://www.bayut.com/to-rent/property/dubai//']

    def parse(self, response):
        for link in response.css('div._4041eb80'):
            yield response.follow(pages,callback=self.parse_data)
                
        for link in response.css('a.b7880daf'):
            if link.css("a.b7880daf").attrib['title']=="Next":
                next_page=link.css('a.b7880daf').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse,dont_filter=True)
            
    def parse_data(self,response):
        for ref in response.css('span._812aa185'):
            if ref.css('span._812aa185').attrib['aria-label']=='Reference':
                author['property_id']=ref.css('span._812aa185::text').get()
            if ref.css('span._812aa185').attrib['aria-label']=='Purpose':
                author['purpose'] =ref.css('span._812aa185::text').get()
            if ref.css('span._812aa185').attrib['aria-label']=='Type':
                author['type'] =ref.css('span._812aa185::text').get()
            if ref.css('span._812aa185').attrib['aria-label']=='Reactivated date':
                author['added_on'] =ref.css('span._812aa185::text').get()
            if ref.css('span._812aa185').attrib['aria-label'] == 'Furnishing':
                author['furnishing'] = ref.css('span._812aa185::text').get()
        price={"currency": None,"amount":None}
        if response.css('span.e63a6bfb').attrib['aria-label']=='Currency':
            price["currency"]= response.css('span.e63a6bfb::text').get()
        if response.css('span._105b8a67').attrib['aria-label'] == 'Price':
            price["amount"]=response.css('span._105b8a67::text').get()
        author['price']=price
        if response.css("div._1f0f1758::text").get()!=None:
            author['location']=response.css("div._1f0f1758::text").get()
        bed_bath_size={"bedrooms":None,"bathrooms":None,"size":None }
        a=response.css("span.fc2d1086::text").getall()
        if a[0]!=None:
            bed_bath_size["bedrooms"] = a[0]
        if a[1]!=None:
            bed_bath_size["bathrooms"] = a[1]
        if response.css("span.fc2d1086 span::text").get()!=None:
            bed_bath_size["size"]=response.css("span.fc2d1086 span::text").get()
        author['bed_bath_size']=bed_bath_size
        if response.css('span.ff863316::text').getall()!=None:
            a=response.css('span.ff863316::text').getall()
            author["permit_number"]=a[-1]
        if response.css('span._55e4cba0').attrib['aria-label']=='Agent name':
            author['agent_name']=response.css('span._55e4cba0::text').get()
        if response.css('img.bea951ad').attrib['src']!=None:
            author["image_url"]=response.css('img.bea951ad').attrib['src']
        if response.css('span._327a3afc::text').getall()!=None:
            a=response.css('span._327a3afc::text').getall()
            author['breadcrumbs']=">".join(a[1:])
        if response.css('span._005a682a::text').getall()!=None:
            author['amenities']=response.css('span._005a682a::text').getall()
        if response.css("span._2a806e1e::text").getall()!= None:
            author["description"]=" ".join(response.css("span._2a806e1e::text").getall())
        yield author
