from selenium import webdriver

'''
    简单测试webchrome的用法
'''
# chrome = webdriver.Chrome()
# chrome.get('http://www.baidu.com')
# chrome.save_screenshot('crawler_file/yimintest.png')
# html = chrome.page_source
# print(html)
# chrome.quit()

'''
    简单测试webdriver的无头使用
'''

options = webdriver.ChromeOptions()
options.add_argument('--headless')
chrome = webdriver.Chrome(chrome_options=options) # 所谓无头，就是不打开浏览器，直接执行
# chrome = webdriver.Chrome()
chrome.get('https://cn.bing.com/') # 默认的首页
chrome.find_element_by_id('sb_form_q').send_keys('theshy') #  在搜索框中搜索python关键字
chrome.find_element_by_id('sb_form_go').click() # 点击搜索

html = chrome.page_source
print(html)
chrome.quit()

