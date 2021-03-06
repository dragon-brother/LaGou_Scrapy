# -*- coding: utf-8 -*-

# Scrapy settings for LaGou_Scrapy project

BOT_NAME = 'LaGou_Scrapy'

SPIDER_MODULES = ['LaGou_Scrapy.spiders']
NEWSPIDER_MODULE = 'LaGou_Scrapy.spiders'

# Referer的Urlencode变量
REFERER_NAME = "大数据"

# 拉钩网登陆账号密码
USERNAME = ""
PASSWORD = ""

# 页码起始值
START_PAGE_NUM = 1

# MONGODB配置
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_USER = ""
MONGODB_PASS = ""
MONGODB_DB_NAME = "fwwb"
MONGODB_COLLECTION = "LaGou"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# COOKIES(enabled by default)
COOKIES_ENABLED = True

# 重定向
REDIRECT_ENABLED = False

# 重试
RETRY_ENABLED = True
RETRY_TIMES = 2
RETRY_HTTP_CODES = [302]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Download中间件的配置
DOWNLOAD_DELAY = 1

# DownloadTimeout Middleware的配置 默认是180秒
DOWNLOAD_TIMEOUT = 20

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 5
# CONCURRENT_REQUESTS_PER_IP = 16

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    'LaGou_Scrapy.middlewares.LagouScrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'LaGou_Scrapy.middlewares.LagouScrapyUserAgentMiddleware': 400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
ITEM_PIPELINES = {
   'LaGou_Scrapy.pipelines.LagouScrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 20
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 0.5
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
