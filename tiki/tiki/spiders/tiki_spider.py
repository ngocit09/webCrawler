import re
from pprint import pprint

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tiki.items import TikiItem


class TikiSpider(CrawlSpider):
    name = 'tiki_spider'
    allowed_domains = ['tiki.vn']
    logger = ''
    rules = (Rule(LinkExtractor(), callback='parse_page'),)

    def get_money(self, string):
        if not string:
            return 0

        return re.findall('\d+\.\d+|\d+', string)[0]

    def get_number(self, string):
        if not string:
            return 0
        res = re.findall('\d+', string)
        if not res:
            return 0

        return res[0]

    def parse_page(self, response):
        search_results = response.css('div.product-box-list > div')

        for item in search_results:
            tiki = TikiItem()
            tiki['item_id'] = item.css('a::attr(data-id)').extract_first()
            tiki['link'] = item.css('a::attr(href)').extract_first()
            tiki['images'] = item.css('.product-image::attr(src)').extract()
            tiki['comment'] = self.get_number(
                item.css('.review::text').extract_first()
            )
            tiki['discount'] = self.get_number(
                item.css('.sale-tag-square::text').extract_first()
            )
            tiki['display_price'] = self.get_money(item.css(
                '.final-price::text').extract_first())
            tiki['price'] = self.get_money(
                item.css('.price-regular::text').extract_first())
            tiki['rating'] = self.get_number(
                item.css('.rating-content>span::attr(style)').extract_first()
            )
            tiki['title'] = ''.join(item.css('.title::text').extract()).strip()
            yield tiki
