from fake_useragent import UserAgent
import requests

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
proxies = {
    "http:":"http://398707160:j8inhg2g@120.27.224.41:16818"
}
response = requests.get(url, headers = headers, proxies = proxies)
print(response.text)