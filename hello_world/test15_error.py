from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.error import URLError

url = "http://www.sx123t.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}

'''对于可能出现的异常，我们使用抓捕异常的方式'''
try:
    req = Request(url, headers=headers)
    resp = urlopen(req)
    print(resp.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args[0].errno)
print("访问完成")