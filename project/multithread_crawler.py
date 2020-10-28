import threading
from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree

'''
    对于写这两个类，都要继承线程类, 也就是override run方法
'''
# 爬虫类
class CrawInfo(Thread):
    '''一个爬虫的buffer，一个用于处理爬下来数据的buffer,一种类似生产者消费者的模式'''
    def __init__(self, url_queue, html_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.html_queue = html_queue
    def run(self):
        headers = {
            "User_Agent":UserAgent().random
        }
        '''当爬虫任务buffer不为空，则取任务执行'''
        while self.url_queue.empty() == False:
            url = self.url_queue.get()
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)

# 解析任务类
class ParseInfo(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue
    def run(self):
        while self.html_queue.empty() == False:
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            lock = threading.Lock()
            with open('duanzi.txt', 'a', encoding='utf-8') as f:
                with lock:
                    for span in span_contents:
                        info = span.xpath('string(.)')
                        f.write(info + '\n')

if __name__ == '__main__':
    # 存储爬虫任务的容器
    url_queue = Queue()
    # 存储解析任务的容器
    html_queue = Queue()
    base_url = 'https://www.qiushibaike.com/text/page/{}/'
    # 选择爬下1到13页
    for i in range(1, 14):
        new_url = base_url.format(i)
        url_queue.put(new_url)
    # 床架哪一个爬虫list
    crawl_list = []
    # 假设只有三个consumers来并行处理爬虫任务
    for i in range(0, 3):
        crawl1 = CrawInfo(url_queue, html_queue)
        crawl_list.append(crawl1)
        crawl1.start()

    # 当爬虫任务完成后与主线程合并
    for crawl in crawl_list:
        crawl.join()

    # 同样的操作对解析任务也做一遍
    parse_list = []
    for i in range(0, 3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()
    for parse in parse_list:
        parse.join()


