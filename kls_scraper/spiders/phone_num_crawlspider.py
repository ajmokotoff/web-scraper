import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from kls_scraper.items import PhoneNumItem

class MySpider(CrawlSpider):
    name = "phonenums"  # The name of this spider

    # The allowed domain and the URLs where the spider should start crawling:
    allowed_domains = ['klsdiversified.com']
    start_urls = ['https://klsdiversified.com/']

    # Rules for which links to assign to parse_item
    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    # Parse webpage with regex in search of a phone number
    def parse_item(self, response):
        self.logger.info('At webpage: %s', response.url)
        for phone_num in response.xpath('//body').re(r'\d{3}.\d{3}.\d{4}'):
            item = PhoneNumItem()
            item['phone_num'] = phone_num
            yield item
