import scrapy
from ..items import DoubanItem

class Douban250Spider(scrapy.Spider):
    name = "douban250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        # 电影名
        names = response.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/span[1]/text()').getall()
        # 电影评分
        scores = response.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[2]/div/span[2]/text()').getall()
        # 详情链接
        links = response.xpath('//*[@id="content"]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a/@href').getall()
        print(links)
        for name, score, link in zip(names, scores,links):
            douban_item = DoubanItem()
            douban_item['name'] = name
            douban_item['score'] = score
            yield scrapy.Request(url=link, callback=self.parse_detail,meta={'movie': douban_item})

        next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').get()    
        
        # yield response.follow(next_url, callback=self.parse)

    def parse_detail(self, response):
        movie = response.meta['movie']
        movie_detail = response.xpath('//*[@id="link-report-intra"]/span[1]/')
        response.meta['movie']['details'] = movie_detail
        print(movie_detail)
        yield movie