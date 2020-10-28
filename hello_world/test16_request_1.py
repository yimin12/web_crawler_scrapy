import requests
from fake_useragent import UserAgent

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":UserAgent().chrome
}
url = "https://www.baidu.com/s"
params = {
    "wd" : "尚学堂"
}
response = requests.get(url, headers = headers, params = params)
print(response.text)
