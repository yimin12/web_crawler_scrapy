from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = "http://httpbin.org/get"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": UserAgent().chrome
}
request = Request(url, headers=headers)
# handler = ProxyHandler({"http": "username:password@ip:port"}) 格式如左边所示，自己独立的代理地址
handler = ProxyHandler({"http": "398707160:j8inhg2g@120.27.224.41:16818"})
# handler = ProxyHandler({"http": "ip:port"}) 使用别人公共的代理地址
handler = ProxyHandler({"http": "118.190.95.43:9001"})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
