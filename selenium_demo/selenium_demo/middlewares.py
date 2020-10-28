from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        url = request.url
        spider.chrome.get(url)
        html = spider.chrome.page_source
        return HtmlResponse(url=url, body=html, request=request, encoding='utf-8')