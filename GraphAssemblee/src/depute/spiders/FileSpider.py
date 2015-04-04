import scrapy
from depute.items import DeputeItem
from scrapy.selector import HtmlXPathSelector
from scrapy import log

class FileSpider(scrapy.Spider):
    name='LinkSpider'
    allowed_domains = 'http://www.elus20.fr/'
    start_urls = ['http://www.elus20.fr/deputes-web-facebook-twitter/']
    arch_urls = 'http://www.elus20.fr/deputes-web-facebook-twitter/?limitstart='
    for i in range(17,700,17):
        start_urls.append(arch_urls + str(i))
        
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        link = hxs.select('//td//div[@class="cbUserListFieldLine"]//span[@class="cbListFieldCont cbUserListFC_name"]//a[@href]').extract()
        for l in link:
            item = DeputeItem()
            item['link'] = l
            yield item
        