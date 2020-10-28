from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 要想调用键盘按键操作需要引入keys包

'''start'''
# 调用环境变量指定的Chrome浏览器创建浏览器对象
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.implicitly_wait(100) # 隐式等待,加载完成直接执行，否则超过时间抛出异常

# 获取页面名为 wrapper的id标签的文本内容
data = driver.find_element_by_id("wrapper").text
print(data)
print(driver.title) # 打印页面标题 "百度一下，你就知道"

driver.find_element_by_id("kw").send_keys("YiminHuang")# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id("su").click()# id="su"是百度搜索按钮，click() 是模拟点击
driver.save_screenshot("Yimin.png")

print(driver.page_source) # 打印网页渲染后的源代码
print(driver.get_cookies()) # 获取当前页面Cookie

'''开始于百度首页进行交互'''
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')# ctrl+a 全选输入框内容

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')

# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("python爬虫")

# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
driver.find_element_by_id("kw").clear()

# 生成新的页面快照
driver.save_screenshot("python爬虫.png")

# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

'''
4.1 页面交互
仅仅抓取页面没有多大卵用，我们真正要做的是做到和页面交互，比如点击，输入等等。那么前提就是要找到页面中的元素。WebDriver提供了各种方法来寻找元素。例如下面有一个表单输入框
'''
# <input type="text" name="passwd" id="passwd-id" />
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_elements_by_tag_name("input")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")

# 输入内容
element.send_keys("some text")
# 模拟点击某个按键
element.send_keys("and some", Keys.ARROW_DOWN)
# 清空文本
element.clear()
# 元素拖拽
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

# 历史记录
driver.forward()
driver.back()

# 关闭浏览器
driver.quit()
