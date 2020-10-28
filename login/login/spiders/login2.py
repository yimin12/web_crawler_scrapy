# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['sxt.cn']
    # start_urls = ['http://www.sxt.cn/index/login/login.html']

    def start_requests(self):
        cookie_str = 'UM_distinctid=163d8c88a6740c-01c2fe892f8d8c-737356c-100200-163d8c88a682a2; 53gid2=10466932807008; 53revisit=1528350416275; acw_tc=AQAAAEcrFECtaA0AoCEscVts5R/jxRhD; CNZZDATA1261969808=52059414-1528348034-%7C1533101043; PHPSESSID=laq5c8frak10hiaj8aq469g3o7; visitor_type=old; 53gid0=10466932807008; 53gid1=10466932807008; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_land_page=http%253A%252F%252Fwww.sxt.cn%252F; kf_72085067_land_page_ok=1; 53kf_72085067_keyword=http%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html'
        cookies={}
        for cookie in cookie_str.split(','):
            key, value = cookie.split("=",1)
            cookies[key.strip()] = value.strip()
        yield scrapy.Request('http://www.sxt.cn/index/user.html', cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)
