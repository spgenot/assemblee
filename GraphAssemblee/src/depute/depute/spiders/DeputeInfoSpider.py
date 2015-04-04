from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from nettuts.items import NettutsItem
from scrapy.http import Request

class DeputeInfoSpider(BaseSpider):
    name = "DeputeInfo"
    allowed_domains    = ["http://www.elus20.fr/"]
   
    #start_urls    = 

    def parse(self, response):
        hxs     = HtmlXPathSelector(response)
        item = DeputeInfoItem()
        item["party"] = hxs.select('//td[@id="cbfv_55"]/text()').extract()
        item["name"] = hxs.select('//h1[@class="title"]/span/span/text()').extract()
        item["twitter"] = hxs.select('//td[@id="cbfv_60"]/a[@href]').extract()
        yield item