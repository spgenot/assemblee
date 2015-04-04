# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeputeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    partie = scrapy.Field()
<<<<<<< HEAD:GraphAssemblee/src/depute/items.py
    
=======
    pass

class DeputeInfoItem(scrapy.Item):
    name = scrapy.Field()
    party = scrapy.Field()
    twitter = scrapy.Field()
>>>>>>> 8d36f49d93d1c057233bc9ea2658907a51fb375c:GraphAssemblee/src/depute/depute/items.py
