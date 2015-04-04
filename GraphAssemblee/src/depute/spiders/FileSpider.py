import scrapy
from depute.items import DeputeItem
from scrapy.selector import HtmlXPathSelector
from scrapy import log

class FileSpider(scrapy.Spider):
    name='LinkSpider'
    allowed_domains = 'http://www.elus20.fr/'
    start_urls = ['http://www.elus20.fr/deputes-web-facebook-twitter/']
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        link = hxs.select('//td//div[@class="cbUserListFieldLine"]//span[@class="cbListFieldCont cbUserListFC_name"]//a[@href]').extract()
        for l in link:
            item = DeputeItem()
            item['link'] = l
            yield item
        