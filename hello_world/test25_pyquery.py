from pyquery import PyQuery as pq
import requests
from fake_useragent import UserAgent

# url = "http://www.xicidaili.com/nn/"
# headers = {
#     "User-Agent": UserAgent().random
# }
#
# response= requests.get(url, headers = headers)
# doc = pq(response.text)
# trs = doc('#ip_list tr')
# for num in range(1, len(trs)):
#     ip = trs.eq(num).find('td').eq(1).text()
#     port = trs.eq(num).find('td').eq(2).text()
#     type = trs.eq(num).find('td').eq(5).text()
#     print(ip, ":", port, "-----", type)


# p = pq("<head><title>hello</title></head>")
# print(p('head').html())  # 返回<title>hello</title>
# print(p('head').text()) # 返回hello
#
# d=pq('<div><p>test 1</p><p>test 2</p></div>')
# print(d('p'))  # <p>test 1</p><p>test 2</p>
# print(d('p').html()) # 注意：当获取到的元素不只一个时，html()方法只返回首个元素的相应内容块, test 1
#
# # 4.eq(index) ——根据给定的索引号得到指定元素。接上例，若想得到第二个p标签内的内容，则可以：
# print (d('p').eq(1).html()) #返回test 2

# 5.filter() ——根据类名、id名得到指定元素，例：
# d=pq("<div><p id='1'>test 1</p><p class='fuck'>test 2</p></div>")
# print(d('p').filter('#1')) # 可以使用css的id选择器
# print(d('div').find('.fuck'))


html='''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
<div>
    <p id='1'>test 1</p>
    <p class='fuck'>test 2</p>
</div>
'''
# d=pq(html)
# print(d('.list').find('.item-0'))  # 也可以使用类选择器
# print(d('div').find('.fuck'))
# item=doc(".list")
# list = item.find(".item-1")
# print(list)
# print(type(item))
# print(item)

# 6.find() ——查找嵌套元素，例：
d=pq("<div><p id='1'>test 1</p><p class='2'>test 2</p></div>")
print(d('div').find('p'))#返回[<p#1>, <p.2>]
print(d('div').find('p').eq(0))#返回[<p#1>]

# 7.直接根据类名、id名获取元素，例：
d = pq("<div><p id='1'>test 1</p><p class='what'>test 2</p></div>")
print(d('#1').html())  # 返回test 1
print(d('.what').html())  # 返回test 2

# 8.获取属性值，例：
d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
print(d('a').attr('href')) # 返回http://hello.com
print(d('p').attr('id')) # 返回my_id

print(d('a').attr('href', 'http://baidu.com')) # 把href属性修改为了baidu

# 10.addClass(value) ——为元素添加类，例：
d=pq('<div></div>')
print(d.addClass('my_class'))#返回[<div.my_class>]

# 11.hasClass(name) #返回判断元素是否包含给定的类，例：
d = pq("<div class='my_class'></div>")
print(d.hasClass('my_class'))  # 返回True

# 12.children(selector=None) ——获取子元素，例：
d = pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
print(d.children())  # 返回[<p#1>, <p#2>]
print(d.children('#2')) # 返回[<p#2>]

# 13.parents(selector=None)——获取父元素，例：
d = pq("<span><p id='1'>hello</p><p id='2'>world</p></span>")
print(d('p').parents())  # 返回[<span>]
print(d('#1').parents('span'))  # 返回[<span>]
print(d('#1').parents('p'))  # 返回[]

# 16.nextAll(selector=None) ——返回后面全部的元素块，例：
d=pq("<p id='1'>hello</p><p id='2'>world</p><img scr='' />")
print(d('p:first').nextAll()) # 返回[<p#2>, <img>]
print(d('p:last').nextAll()) # 返回[<img>]

# 17.not_(selector) ——返回不匹配选择器的元素，例：
d=pq("<p id='1'>test 1</p><p id='2'>test 2</p>")
print(d('p').not_('#2')) # 返回[<p#1>]