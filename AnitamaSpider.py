# -*- coding: utf-8 -*-

import requests
import os
from bs4 import BeautifulSoup
import re

path = __Where_you_want_to_put_articles_in+"/" #文件路径
main = 'http://www.anitama.cn/'


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"


def find_article_url(page):
    url = main+'channel/all/'+str(page)
    r = getHtmlText(url)
    print('page:'+str(page))
    soup = BeautifulSoup(r, 'lxml')
    article_url = re.findall(
        r'article/[0-9a-f]*', str(soup.find_all(id="area-article-channel")))
    for i in range(len(article_url)):
        article_url[i] = main+article_url[i]
    return article_url


def download(article_url):
    flag = 1
    for aurl in article_url:
        r = getHtmlText(aurl)
        soup = BeautifulSoup(r, 'lxml')
        with open(path+"Article/"+soup.title.get_text().replace("/", "")+".html", "w") as f:
            f.write(soup.find(id="area-title-article").prettify())
            f.write(soup.find(id="area-content-article").prettify())
            f.write(soup.find(id="area-copyright-article").prettify())
        print("Success *"+str(flag))
        flag = flag+1


if __name__ == '__main__':
    article_url = []
    for page in range(1, 301):
        article_url.extend(find_article_url(page))
    download(article_url)