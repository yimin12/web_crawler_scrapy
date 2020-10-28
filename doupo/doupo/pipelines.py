# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoupoPipeline:

    def open_spider(self, spider):
        self.file = open('file/yuanzun.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        info = '\n'+ title + '\n' + content + '\n'
        # info = title + '\n'
        self.file.write(info)
        self.file.flush()
        return item

    def close_spider(self, spider):
        self.file.close()