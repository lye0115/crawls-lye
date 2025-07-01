import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BiqugeItem


class BqgSpider(CrawlSpider):
    name = "bqg"
    allowed_domains = ["www.biqooge.com"]
    start_urls = ["https://www.biqooge.com/23_23822/"]

    rules = (Rule(LinkExtractor(allow=r"23_23822/(.*?).html"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = BiqugeItem()
        item['title'] = response.xpath('//*[@id="wrapper"]/div[5]/div/div[2]/h1/text()').get()
        item['content'] = response.xpath('//*[@id="content"]').getall()
        yield item

