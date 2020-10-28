from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

args={
    "wd":"Theshy",
    "ie":"utf-8"
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))
print(url)
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent" : UserAgent().random
}
request = Request(url,headers = headers)
response = urlopen(request)
info = response.read()
print(info.decode())