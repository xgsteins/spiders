# https://www.zerochan.net/ 这个图片网站的爬虫


import requests
import os
import re

path = 'F:\\pictures\\Nagato\\'
main = 'https://www.zerochan.net/'
key = input('输入一个搜索关键词:')
page = 1  # 设置起始页码
name = 1
while 1:  # 下载图片
    url = main+key+'?p='+str(page)  # 搜索结果页面
    r = requests.get(url)  # 连接网页
    strurl = re.findall(
        r'https://static.zerochan.net/[.a-z0-9A-Z]*.jpg', r.text)
    flag = 0
    print(strurl)
    for jpgUrl in strurl:
        print(jpgUrl+' start!')
        flag = 1
        r = requests.get(jpgUrl)
        with open(path+str(name)+'.jpg', 'wb') as f:
            f.write(r.content)
        f.close()
        print(jpgUrl+' ok\n')
        name = name+1
    if flag == 0:
        break
    page += 1  # 下一页
