from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
url = 'https://www.huya.com/g/lol'
driver.get(url)
num = 1
while True:
    print('Page : ' + str(num) + "------------------------------------------")
    num += 1
    sleep(5)
    html = driver.page_source
    names = driver.find_elements_by_xpath('//i[@class="nick"]')
    counts = driver.find_elements_by_xpath('//i[@class="js-num"]')
    for name, count in zip(names,counts):
        print(name.text,":",count.text)
    if driver.page_source.find('laypage_next') != -1:
        driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
    else:
        break
driver.quit()