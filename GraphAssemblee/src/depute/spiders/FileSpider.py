import scrapy
#from depute.depute.items import DeputeItem

class FileSpider(scrapy.Spider):
    name='LinkSpider'
    allowed_domains = 'http://www.elus20.fr/'
    start_url = ['http://www.elus20.fr/deputes-web-facebook-twitter/?limitstart=17',
                 'http://www.elus20.fr/deputes-web-facebook-twitter/']
    arch_url = 'http://www.elus20.fr/deputes-web-facebook-twitter/?limitstart='
    def parse(self, response):
        for sel in response.xpath('//td//div[@class="cbUserListFieldLine"]'):
            item = DeputeItem()
            item['link'] = sel.xpath('//span[@class="cbListFieldCont cbUserListFC_name"]//a[@href]').extract()
            item['partie']=sel.xpath('//span[@class="cbListFieldCont cbUserListFC_avatar"]//img//@alt').extract()
            yield item
        