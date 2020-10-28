import json

# 将字符串转换成key，value形式的字典
str = '{"name":"盗梦空间"}'
print(type(str))
obj = json.loads(str)
print(type(obj))
print(obj)

# 再将字典的内容转换成为字符串
str2 = json.dumps(obj, ensure_ascii=False)
print(type(str2), " : ", str2)

json.dump(obj, open("crawler_file/movie.txt",'w',encoding='utf-8'), ensure_ascii=False)
str3 = json.load(open("crawler_file/movie.txt", encoding='utf-8'))
print(str3)
