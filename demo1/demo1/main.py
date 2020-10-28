from scrapy.cmdline import execute

# 爬下百度官网的数据
# execute('scrapy crawl baidu'.split())
'''
    或者另外一种写法
    execute(['scrapy', 'crawl', 'baidu'])
'''

# 爬下"起点"的数据
execute('scrapy crawl qidian'.split())

# 爬下"猫眼"的数据
# execute('scrapy crawl maoyan'.split())