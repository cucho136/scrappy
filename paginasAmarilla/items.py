# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaginasamarillaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    address= scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    ZIP = scrapy.Field()
    phone = scrapy.Field()
