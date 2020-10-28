# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    # start_urls = ['https://www.qidian.com/rank/yuepiao']

    # 如果你想爬取多个页面的数据可以自己设置url（如，post的请求中的数据拼接，或者爬取多个url
    def start_requests(self):
        base_url ='https://www.qidian.com/rank/yuepiao?page={}'
        for i in range(1,6):
            yield scrapy.Request(base_url.format(i))

    def parse(self, response):
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        for name, author in zip(names, authors):
            print(name,':',author)

        # 封装成book返回出去
        # book = []
        # for name, author in zip(names, authors):
        #     book.append({'name':name, 'author':author})
        # return book