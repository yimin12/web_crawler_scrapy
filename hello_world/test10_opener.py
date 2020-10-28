from urllib.request import Request,build_opener, HTTPHandler
from fake_useragent import UserAgent


url = "http://www.baidu.com"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":UserAgent().chrome
}
request = Request(url, headers = headers)
handlers = HTTPHandler()
opener = build_opener(handlers)
response = opener.open(request)
print(response.read().decode())