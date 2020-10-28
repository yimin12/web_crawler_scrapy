from urllib.request import Request, urlopen, HTTPCookieProcessor, build_opener
from fake_useragent import UserAgent
from urllib.parse import urlencode

# step 1:找到登陆页面的form表单
login_url = "http://www.sxt.cn/index/login/login"
headers = {
    "User-Agent": UserAgent().chrome
}
# step 2:填写好表单的登陆数据
form_data = {
    "user" : "1770318143",
    "password" : "123456"
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers = headers, data=f_data)
# step 3:记录cookie
handler = HTTPCookieProcessor()
opener = build_opener(request)
info_url = "http://www.sxt.cn/index/user.html"
request = Request(info_url, headers = headers)
response = opener.open(request)
print(response.read().decode())