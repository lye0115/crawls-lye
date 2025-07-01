# Scrapy settings for mail project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "mail"

SPIDER_MODULES = ["mail.spiders"]
NEWSPIDER_MODULE = "mail.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "mail (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
   "Cookie": "RK=BX/g+bYXMv; ptcz=b803397f512f3b3d901d11d75e36ef737dafb41d97904e2de00e8425c022922d; qm_device_id=TNuX9tXj8t4dO0n2ROvb5dJCbBZMdHPsQ9aAXybDQcoBl+txAU6CRJLiB9zS6vuX; edition=mail.qq.com; qm_logintype=qq; p_uin=o0735039922; xm_pk=13102661759914418&ShIxY1OkRsSWGX23LVCzwwAA; xm_ptk=13102661759914418&CAESILz7zJ4ls4D2vQwmH7bWlxsU/Qlu2YhK7IxHaFMFFUKe; qm_username=735039922; qm_domain=https://mail.qq.com; ssl_edition=sail.qq.com; username=735039922&735039922; xm_uin=13102661759914418; skey=@82VGDDRKd; pt4_token=f5VWx4s5MLdGa7346hkM6DzVFyXloMibXa4QfAs65UA_; xm_envid=456_owx6TY8E35FEVo2fZlbN8medhPegXwMaxVw+jTB3tLTqm9rEFaP/cuj+DxChrNZNJcJk8j9m84zSkZQI7uUbYmZ4uUkKMjLn+Szaw5GurXrvVa7HrWHP8vD//40FUqtXCmiqNXzlIkV7PRd1zbe9q6CTHcaTjDQc5oPJuixW; xm_pcache=13102661759914418&V2@UPo7ysHUSrmouWQSqmcuwwAA@0; uin=o735039922; sid=735039922&a27e2ed6b9759296c13ec95713f159bf,qcGdzM0kxQTJpV3l6eEV6WUZhWnpoak55b3MyNGlZWGtFbE1PTnV6N21FNF8.; qm_muti_sid=13102661759914418&zX8Tu2q3DcKdXHcQ; xm_sid=zbJRdozRNUguz01YACs0cgAA; xm_muti_sid=13102661759914418&zbJRdozRNUguz01YACs0cgAA; xm_skey=13102661759914418&5a4f49061c9975cd38fa81c083aa63db; xm_ws=13102661759914418&1c694b98df2ac9aebddb5f370bd3b791; xm_data_ticket=13102661759914418&CAESIGdf3WsALozNK8_RsnsfXDpzsO5mvEafRPcSmCDjWp7X; CCSHOW=000001"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "mail.middlewares.MailSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "mail.middlewares.MailDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "mail.pipelines.MailPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
