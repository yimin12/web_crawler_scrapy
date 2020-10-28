from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

def get_html(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent":UserAgent().chrome
    }
    request = Request(url,headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()

def save_html(filename, html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)

def main():
    content = input("请输入要下载的内容：")
    num = input("请输入要下载多少页：")
    base_url = "http://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        filename = "第" + str(pn + 1) + "页.html"
        args = urlencode(args)
        print("正在下载" + filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename, html_bytes)


if __name__ == '__main__':
    main()