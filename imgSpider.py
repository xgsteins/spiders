# https://www.zerochan.net/ 这个图片网站的爬虫

import requests
import os
import re
import hashlib

path = input('输入想要存放图片的文件夹')
key = input('输入一个搜索关键词:')
main = 'https://www.zerochan.net/'
page = 1  # 设置起始页码
name = 1  #文件名
imgSet = set()
while 1:  # 下载图片
    url = main+key+'?p='+str(page)  # 搜索结果页面
    r = requests.get(url)           # 连接网页
    strurl = re.findall(
        r'https://static.zerochan.net/[.a-z0-9A-Z]*.jpg', r.text)   # 正则匹配
    flag = 0
    strurl = set(strurl)
    # print(strurl)
    for jpgUrl in strurl:
        print(jpgUrl+' start!')
        flag = 1
        r = requests.get(jpgUrl)
        h = hashlib.md5(r.content).hexdigest()
        if h not in imgSet:
            imgSet.add(h)
            with open(path+key+str(name)+'.jpg', 'wb') as f:
                f.write(r.content)
            f.close()
            print(jpgUrl+' ok\n')
            name = name+1
    if flag == 0:
        break
    page += 1  # 下一页
