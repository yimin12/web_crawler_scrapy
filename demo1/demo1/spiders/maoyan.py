# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        scores_div = response.xpath('//div[@class="channel-detail channel-detail-orange"]')
        scores = []
        for score in scores_div:
            scores.append(score.xpath('string(.)').extract_first())
        # for name, score in zip(names, scores):
            # print(name,":",score)
            '''
            如果要推送数据到pipelines，只能使用items的对象或者dict字典对象
            '''
            # yield {'name':name,'score':score}
        item = MovieItem()
        for name,score in zip(names, scores):
            item['name'] = name
            item['score'] = score
            yield item