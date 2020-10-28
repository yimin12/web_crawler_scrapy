# -*- coding: utf-8 -*-
import scrapy


class Guazi3Spider(scrapy.Spider):
    name = 'guazi3'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/bj/buy/']

    def parse(self, response):
        pass
