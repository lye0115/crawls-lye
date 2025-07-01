import scrapy


class QmailSpider(scrapy.Spider):
    name = "qmail"
    allowed_domains = ["mail.qq.com"]
    start_urls = ["https://mail.qq.com/cgi-bin/frame_html?sid=zX8Tu2q3DcKdXHcQ&r=0d78716b4dc2164f8565b6f128ac2795&lang=zh"]

    def parse(self, response):
        print(response.text)
