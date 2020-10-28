# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Demo1Pipeline(object):
    '''如同过滤器一般，按顺序执行'''
    def open_spider(self, spider):
        self.filename = open('file/movie.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # with open('movie.txt', 'a', encoding='utf-8') as f:
        #     f.write(json.dumps(item, ensure_ascii=False) + '\n')
        # print(item)
        self.filename.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def close_spider(self, spider):
        self.filename.close()

