from selenium import webdriver
from lxml import etree
from time import sleep

url = 'https://search.jd.com/Search?keyword=ipad%20pro&enc=utf-8&wq=ipad%20pro&pvid=5701887b1bb145cca50b489fea75584d'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options=options)
chrome.get(url)

'''有些页面需要滚动才通过ajax发送异步请求, 只要一定超过底部位置的数就一定会滑到底'''
js = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js)
sleep(3)
html = chrome.page_source
e = etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')

for name,price in zip(names,prices):
    print(name.xpath('string(.)'),":",price)
chrome.quit()
