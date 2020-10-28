import re
str1 = "I study Python3.8 EveryDay"
print("-----------match()---------------")
# 匹配字符，使用正则表达式
m1 = re.match(r'I', str1)
m2 = re.match(r'\w',str1)
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'i', str1, re.I)
m6 = re.match(r'\S', str1)
# m7 = re.match(r'Study', str1)  # 匹配不到，因为match是从左开始匹配
print(m6.group())
print("-------------search()-----------------")
s1 = re.search(r'study', str1)
s2 = re.search(r's\w+', str1)
# 匹配Python3.6
s3 = re.search(r'P\w+.\d', str1)
print(s3.group())
print("-------------findall()-----------------")
# 查找所有y
f1 = re.findall(r'y', str1)
print(f1)
print("-------------test()-----------------")
str2 = '<div><a href="http://www.bjsxt.com">bjsxt尚学堂</a></div>'
# 提取a标签的内容
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2) # 选取所有中文信息
t2 = re.findall(r'<a href="http://www.bjsxt.com">(.+)</a>', str2) #提取href标签后面的元素
# 提取herf
t3 = re.findall(r'<a href="(.+)">', str2)
print(t3)
print("-------------sub()-----------------")
# 将str2的div换成span
su1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)
print(su1)
