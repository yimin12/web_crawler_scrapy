from urllib.request import  Request, urlopen
from urllib.parse import quote

url = "https://www.baidu.com/s?wd={}".format(quote("Theshy"))

'''如果出现百度安全认证，需要加入Accept请求头'''
headers= {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
request = Request(url, headers = headers)
response = urlopen(request)
print(response.read().decode())
