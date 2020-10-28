import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
import re

from lxml import etree


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    # sleep(randint(3,5))
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else :
        return None

def parse_index(html):
    e = etree.HTML(html)
    all_url = e.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[2]/a/@href')
    print(all_url)
    return ['http://maoyan.com{}'.format(url) for url in all_url]

def parse_info(html):
    e = etree.HTML(html)
    name = e.xpath("//h1[@class='name']/text()")[0]
    types = e.xpath('//li[@class="ellipsis"][1]/text()')[0]
    actors = e.xpath("//li[@class='celebrity']/div[@class='info']/a/text()") # 有重复元素
    actors = format_actors(actors)
    return {
        "name":name,
        "types":types,
        "actors":actors
    }

def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.strip())
    return actor_set

def main():
    index_url = 'http://maoyan.com/films?showType=2'
    html = get_html(index_url)
    print(html)
    movie_url = parse_index(html)
    print(movie_url)
    for url in movie_url:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)
if __name__ == '__main__':
    main()