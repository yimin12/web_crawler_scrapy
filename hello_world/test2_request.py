from urllib.request import urlopen
from urllib.request import Request
from random import choice

url = 'http://www.baidu.com'

user_agents = [
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
]

headers={
    "User-Agent":choice(user_agents)
}
request = Request(url,headers=headers)
print(request.get_header('User-agent'))
response =  urlopen(request)
info = response.read()

print(info.decode())