import scrapy
import json
from depute.items import DeputeInfoItem
from scrapy.selector.lxmlsel import HtmlXPathSelector

class DeputeInfoSpider(scrapy.Spider):
    name = "DeputeInfo"
    allowed_domains    = ["http://www.elus20.fr/"]
    
    f = open("../info.json", "r")
    data = json.loads(f.read())
    deputeUrls = []
    for element in data:
        linkValue = element["link"].split("\"")[1]
        if(linkValue not in deputeUrls):
            deputeUrls.append(linkValue)
    f.close()
    
    print(str(len(deputeUrls))+" items founded")
    start_urls = deputeUrls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = DeputeInfoItem()
        item["party"] = hxs.select('//td[@id="cbfv_55"]/text()').extract()
        item["name"] = hxs.select('//h1[@class="title"]/span/span/text()').extract()
        account = hxs.select('//td[@id="cbfv_60"]/a/text()').extract()
        print(account)
        if(len(account) != 0):
            item["twitter"] = account[0].split('/')[-1]
        else:
            item["twitter"] = []
        yield item