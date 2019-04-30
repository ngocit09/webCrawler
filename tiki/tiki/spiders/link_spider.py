import re
from pprint import pprint

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tiki.link_item import LinkItem


class LinkSpider(CrawlSpider):
    name = 'link_spider'
    allowed_domains = ['tiki.vn']
    logger = ''
    start_urls = ['https://tiki.vn']
    rules = (Rule(LinkExtractor(), callback='parse_page'),)

    def parse_page(self, response):
        item = LinkItem()
        item['source'] = response.url
        item['links'] = response.css('a::attr(href)').extract()
        yield item
