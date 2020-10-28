from fake_useragent import UserAgent
import requests

session = requests.Session()
headers = {
    "User-Agent":UserAgent().chrome
}
login_url = "http://www.sxt.cn/index/login/login"
params = {
    "user": "17703181473",
    "password": "123456"
}
response = session.post(login_url, headers = headers, data = params)
info_url = "https://www.sxt.cn/index/user.html"
resp = session.get(info_url, headers = headers)
print(resp.text)