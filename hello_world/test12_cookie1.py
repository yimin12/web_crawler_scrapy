from urllib.request import Request, urlopen
from fake_useragent import UserAgent

'''使用方式1是直接在网页端口登陆好了之后将cookie数据复制下来'''
url = "http://www.sxt.cn/index/user.html"
headers = {
    "User-Agent": UserAgent().chrome,
    "Cookie": "UM_distinctid=163d8c88a6740c-01c2fe892f8d8c-737356c-100200-163d8c88a682a2; 53gid2=10466932807008; 53revisit=1528350416275; 53gid1=10466932807008; acw_tc=AQAAAIktZUa8ZQEAoCEsceTKxzX+LOad; CNZZDATA1261969808=52059414-1528348034-%7C1532407588; PHPSESSID=uh265s5725vojpqdsbagj0n726; visitor_type=old; 53gid0=10466932807008; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=http%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; 53kf_72085067_land_page=http%253A%252F%252Fwww.sxt.cn%252F; kf_72085067_land_page_ok=1"
}
request = Request(url, headers=headers)
response = urlopen(request)

print(response.read().decode())
