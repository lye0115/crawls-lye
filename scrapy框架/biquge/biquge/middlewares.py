# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from .settings import USER_AGENT_LIST
import random

class BiqugeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class BiqugeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

class UAMiddleware:
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        request.headers['Referer'] = 'https://www.biqooge.com/'
        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        request.headers['Cookie'] = 'jieqiVisitTime=jieqiArticlesearchTime%3D1734338728; jieqiVisitId=article_articleviews%3D1103%7C23822; cf_clearance=cK1GtK7HFuASJwD7eelzmQzYKqIzoJDf1GFsl7IdT9s-1734340745-1.2.1.1-Z0yOJC61FVojzXx1i3VvsSQpYhn_0yBnm5aJd41E0FBDdQhvGvoLh8u89SmU9Sf6Yp0Z1LJWbYZKPhTm11bJMw8LKBt1wh311tVcnMvGtbYcYKXpSquGV9UW4d4DnGSI6RoEtC7SA_hcajlZrLjuqkARnItLFBw4mA5t13uUvYgvXA2HEIWOXutydqjd8wYQD8tifHwuagCLGTmTf0ba8iRLziIak9QNYvMkUJYafE0b1WFfZ0Kaup5p98jAto5JVdeAQKs9fy_kWy.wrEh9mM05U63zpwHsk.3sVZGtqIYaBiCAg_fpk9Y6rBodUe1caXl7r9h.33cNLNEMipTrpEaFJniYvMAVBw7If2MuG_6Yfhwb_Zk.G0asP_eRI2RqJQnu0oVO_V7wi22JO4At5ntEHrVIQLnEP4jqyuTzDdyufO6Ui15W2tYgYvfid5Cf'
        proxy_url = "http://127.0.0.1:7897"  # 替换为实际的代理地址和端口
        request.meta['proxy'] = proxy_url
        print('使用了UA中间件')
