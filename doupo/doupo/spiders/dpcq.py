# -*- coding: utf-8 -*-
import scrapy


class DpcqSpider(scrapy.Spider):
    name = 'dpcq'
    allowed_domains = ['ksl']
    start_urls = ['https://www.kanshula.com/book/doupocangqiongzhiwushangzhijing/1156338.shtml']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = "".join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ','\n\t')
        yield {
            'title':title,
            'content':content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[3]/@href').extract_first()
        # base_url = 'https://www.kanshula.com{}'.format(next_url)
       # base_url = response.urljoin(next_url) # 效果根上面一句一样，省的自己拼接错误
        if next_url.find('.shtml') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse, dont_filter=True)