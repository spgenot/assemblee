import scrapy
from depute.items import DeputeItem
from scrapy.selector import HtmlXPathSelector
class FileSpider(scrapy.Spider):
    name='LinkSpider'
    allowed_domains = 'http://www.elus20.fr/'
    start_url = ['http://www.elus20.fr/deputes-web-facebook-twitter/?limitstart=17']
    #arch_url = 'http://www.elus20.fr/deputes-web-facebook-twitter/?limitstart='
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        link = hxs.select('//td//div[@class="cbUserListFieldLine"]//span[@class="cbListFieldCont cbUserListFC_name"]//a[@href]')
        #for sel in response.xpath('//td//div[@class="cbUserListFieldLine"]'):
        for l in link:
            item = DeputeItem()
            item['link'] = l#sel.xpath('//span[@class="cbListFieldCont cbUserListFC_name"]//a[@href]').extract()
            #item['partie']=sel.xpath('//span[@class="cbListFieldCont cbUserListFC_avatar"]//img//@alt').extract()
            yield item
        