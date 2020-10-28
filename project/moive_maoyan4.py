import requests
from fake_useragent import  UserAgent
from random import randint
from time import sleep
from pyquery import PyQuery as pq

def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    sleep(randint(3,5))
    response = requests.get(url, headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_index(html):
    doc = pq(html)
    all_a = doc('.channel-detail.movie-item-title a')
    all_url = []
    for a in all_a:
        all_url.append(a.attrib['href'])
    return ['http://maoyan.com{}'.format(url) for url in all_url]

def parse_info(html):
    doc = pq(html)
    name = doc('h1.name')[0].text
    types = doc('li.ellipsis')[0].text
    actors = doc('li.celebrity > div.info > a')
    actors = format_actors(actors)
    return {
        "name":name,
        "types":types,
        "actors":actors
    }

def format_actors(actors):
    actor_set = set()
    for actor in actors:
        actor_set.add(actor.text.strip())
    return actor_set

def main():
    index_url = 'http://maoyan.com/films'
    html = get_html(index_url)
    movie_urls = parse_index(html)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)

if __name__ == '__main__':
    main()