#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：requests 
@File    ：work.py
@IDE     ：PyCharm 
@Author  ：wdd
@Date    ：2021/3/29 15:51 
'''
import re
import requests
# 3、有一个字符串 'hello,123!!hello,345!' 把 数字都替换为 xiaoming 用re模块进行
str = 'hello,123!!hello,345!'
rusta = re.sub('\d+','xiaoming',str)
print(rusta)
# 4、有一个字符串'hello,world' 用 re模块换成  worldhello
str1 = 'hello,world'
rusta1 = re.sub('(\w+),(\w+)',r'\2\1',str1)
print(rusta1)

# 1、用requests打开论坛首页，用re 获取 左侧所有板块名称
hosts = '47.107.178.45'
session = requests.session()
url_params ={"m":"bbs",
            "c":"forumlist"}
response1 = session.get(url = 'http://%s/phpwind/index.php'%hosts,
                        params = url_params)
txt = response1.text
rusta2 = re.findall('fid=.\d">(.+?)</a>',txt)
print(rusta2)

# 2、用requests打开腾讯首页，用re 模块获取标题栏（新闻、视频、图片等）
response = requests.get(url = 'https://www.qq.com/')
txt = response.text
restu = re.findall('bosszone="dh_\d">(.+?)</a>',txt)
for i in  restu:
    print(i)
