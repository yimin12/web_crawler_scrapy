from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

url = "http://www.sxt.cn/index/login/login.html"
# post 请求通常对应的表单发送，所以一般整理的是账号和密码，然后再利用urlencode整合在一起
form_data = {
    "user": "17703181473",
    "password": "12346"
}
headers = {
    "User-Agent":UserAgent().chrome
}
f_data = urlencode(form_data)
# POST 需要将传输的数据encode才能被识别
request = Request(url,data=f_data.encode(),headers = headers)
response = urlopen(request)
print(response.read().decode())