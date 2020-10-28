# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

# 使用scrapy分布式爬区
class Lianjia2Spider(RedisSpider):
    name = 'lianjia2'
    allowed_domains = ['lianjia.com']
   # start_urls = ['https://bj.lianjia.com/ershoufang/pg{}/'.format(num) for num in range(1, 5)]
    redis_key ='lianjia:start_urls'

    index = 2
    base_url = 'https://bj.lianjia.com/ershoufang/pg{}/'
    # base_url = 'https://bj.lianjia.com/ershoufang/pg1/'

    def parse(self, response):
        urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_info)
        if self.index < 1000:
            yield scrapy.Request(self.base_url.format(self.index),callback=self.parse_info)
        self.index = self.index + 1

    def parse_info(self, response):
        total = response.xpath(
            'concat(//span[@class="total"]/text(),//span[@class="unit"]/span/text())').extract_first()
        unitPirceValue = response.xpath('string(//span[@class="unitPriceValue"])').extract_first()
        xiao_qu = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        qu_yu = response.xpath('string(//div[@class="areaName"]/span[@class="info"])').extract_first()

        base = response.xpath('//div[@class="base"]//ul')
        hu_xing = base.xpath('./li[1]/text()').extract_first()
        lou_ceng = base.xpath('./li[2]/text()').extract_first()
        mian_ji = base.xpath('./li[3]/text()').extract_first()
        zhuang_xiu = base.xpath('./li[9]/text()').extract_first()
        gong_nuan = base.xpath('./li[last()-2]/text()').extract_first()
        chan_quan = base.xpath('./li[last()]/text()').extract_first()

        transaction = response.xpath('//div[@class="transaction"]//ul')
        yong_tu = transaction.xpath('./li[4]/span[2]/text()').extract_first()
        nian_xian = transaction.xpath('./li[last()-3]/span[2]/text()').extract_first()
        di_ya = transaction.xpath('./li[last()-1]/span[2]/text()').extract_first().strip()

        yield {
            "total": total,
            "unitPriceValue": unitPirceValue,
            "xiao_qu": xiao_qu,
            "qu_yu": qu_yu,
            "hu_xing": hu_xing,
            "lou_ceng": lou_ceng,
            "mian_ji": mian_ji,
            "zhuang_xiu": zhuang_xiu,
            "gong_nuan": gong_nuan,
            "chan_quan": chan_quan,

            "yong_tu": yong_tu,
            "nian_xian": nian_xian,
            "di_ya": di_ya
        }
