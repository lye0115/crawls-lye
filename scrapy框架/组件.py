# 引擎:数据和信号的传递
# 调度器：任务队列
# 下载器：发送请求，获取相应，交给引擎
# 爬虫：起始url的解析
# 管道：数据清洗，数据存储
# 中间件：请求和响应的拦截器的定制化操作

# 内置对象
# request对象
# response对象

# 创建项目
# scrapy startproject 项目名
# 创建爬虫
# scrapy genspider -t basic 爬虫名 域名
# 运行爬虫
# scrapy crawl 爬虫名


# 模拟登录
# COOKIES_ENABLED = False 
# 设置请求头
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en",
# }

# POST请求
# scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)


# 中间件
# 下载中间件：请求和响应的拦截器的定制化操作
  # - 请求拦截器：请求的定制化操作，比如添加请求头，设置cookie
  # - 响应拦截器：响应的定制化操作，比如添加请求头
# 爬虫中间件：爬虫的拦截器的定制化操作(不常用，因为它和下载中间件功能基本一样)

# 反爬参数
# USER_AGENT_LIST = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0',
# ]


# scrawlspider --模板
# scrawlspider 能够匹配满足条件的url地址，组装成request对象，交给引擎
# 使用步骤：
# 1. 创建项目
# 2. 创建爬虫
# 3. 修改settings.py文件
# 4. 修改爬虫文件
# 5. 运行爬虫