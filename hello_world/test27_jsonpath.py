from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
import json

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
# '$'代表根目录，从根目录开始，注意根目录不是最外层的那级，而是allCitySearchLabels这级
names = jsonpath(json.loads(response.text), '$..name')
codes = jsonpath(response.json(), '$..code')

print(names)
print(codes)


'''
3.1 json.loads()
 把Json格式字符串解码转换成Python对象 从json到python的类型转化对照如下：

'''
strList = '[1, 2, 3, 4]'
strDict = '{"city": "北京", "name": "范爷"}'
json.loads(strList)
# [1, 2, 3, 4]
json.loads(strDict) # json数据自动按Unicode存储
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u732b'}

''' 
json.dumps()
实现python类型转化为json字符串，返回一个str对象 把一个Python对象编码转换成Json字符串
'''

listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr = {"city": "北京", "name": "范爷"}
json.dumps(listStr)
# '[1, 2, 3, 4]'
json.dumps(tupleStr)
# '[1, 2, 3, 4]'

# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码

json.dumps(dictStr)
# '{"city": "\\u5317\\u4eac", "name": "\\u5927\\u5218"}'

print(json.dumps(dictStr, ensure_ascii=False))
# {"city": "北京", "name": "范爷"}


'''
json.dump()
将Python内置类型序列化为json对象后写入文件
'''
# 对于list和dict而言，json都可以之间转换为python的对象
listStr = [{"city": "北京"}, {"name": "范爷"}]
json.dump(listStr, open("listStr.json","w"),ensure_ascii=False)

dictStr = {"city": "北京", "name": "范爷"}
json.dump(dictStr, open("dictStr.json","w"), ensure_ascii=False)

'''
json.load((
读取文件中json的形式的字符远元素，转换成python类型
'''
strList = json.load(open("listStr.json"))
print(strList)

# [{u'city': u'\u5317\u4eac'}, {u'name': u'\u5927\u5218'}]

strDict = json.load(open("dictStr.json"))
print(strDict)
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u5218'}