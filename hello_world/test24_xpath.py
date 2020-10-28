from lxml import etree
import requests
from fake_useragent import UserAgent

# url = "https://www.qidian.com/rank/yuepiao?chn=21"
# headers = {
#     "User-Agent":UserAgent().chrome
# }
# response = requests.get(url, headers = headers)
# e = etree.HTML(response.text)
# names = e.xpath("//h4/a/text()")
# authors = e.xpath('//p[@class="author"]/a[1]')
# for name, author in zip(names, authors):
#     print(name, ":", author)

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
# lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能。
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result)

# 除了直接读取字符串，还支持从文件读取内容。比如我们新建一个文件叫做 hello.html，内容为
html = etree.parse('crawler_file/hello.html')
result = etree.tostring(html, pretty_print=True)
# print(type(html))
result = html.xpath('//li')
# print(result)
# print (len(result))
# print (type(result))
# print (type(result[0]))

# 获取li所有元素内容
result = html.xpath("//li/@class")
print(result)

# 获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result = html.xpath("//li/a[@href='link1.html']")
print(result)

# 假设我要去span后面的标签， 不能直接使用 result = html.xpath('//li/span')
# 因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
result = html.xpath('//li/a//@class')
print (result)

# 获取最后一个 <li> 的 <a> 的 href
result = html.xpath('//li[last()]/a/@href')
print(result)

# 获取倒数第二个元素的内容
result = html.xpath('//li[last()-1]/a')
print(result[0].text)

# 获取 class 为 bold 的标签名
result = html.xpath('//*[@class="bold"]')
print(result[0].tag)
