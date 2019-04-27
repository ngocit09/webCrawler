# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TikiItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    images = scrapy.Field()
    discount = scrapy.Field()
    display_price = scrapy.Field()
    rating = scrapy.Field()
    comment = scrapy.Field()
