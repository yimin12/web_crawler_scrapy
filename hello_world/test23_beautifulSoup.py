from bs4 import BeautifulSoup
from bs4 import Comment
str='''
<title>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''
bs = BeautifulSoup(str,"lxml")

# print(bs.title)
# print(bs.div)
# print(bs.div.attrs)
# print(bs.div.get('class'))
# print(bs.div['float'])
# print(bs.a['href'])

# 取内容
# print(bs.div.string)
# print(bs.div.text)

#BeautifulSoup对象表示的是一个文档的全部内容，大部分可以把它当tag使用，它支持文档树和搜索文档书中的大部份方法
# print(bs.name)
# print(bs.head.name)
#
# # 取注释的内容
# print(bs.strong.string) # 对于string可以取注释中的内容
# print(type(bs.strong.string))
# print(bs.strong.text) # 对于text，取不出注释的内容
#
# if type(bs.stong.string) == Comment:
#     print(bs.strong.string)
#     print(bs.strong.prettify())
# else:
#     print(bs.strong.text)

print("-----------------------------")
print(bs.find_all('title'))
print(bs.find_all(id='title'))
print(bs.find_all(class_='info'))
print(bs.find_all("div",attrs={'float':'left'}))

print("--------------------css()---------------------------")
print(bs.select('title'))
print(bs.select('#title'))
print(bs.select('.info'))
print(bs.select('div span'))
print(bs.select('div > span'))
print(bs.select('div')[1].select('a'))
print(bs.select('title')[0].text)
