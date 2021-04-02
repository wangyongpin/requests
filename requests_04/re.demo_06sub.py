#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re.demo_06sub.py
# @time: 2021/3/28 10:36

import re
str1 = '135777 666 8899, 贵州号码'
str2 = str1.replace(' ','')
print(str2)
#
result_01 = re.sub('(\d\s+\d)','',str1)
print(result_01)

str1 = '135777  666 8899, 贵州号码' # 多个空格用\s
result_02 = re.sub('(\d+)\s+(\d+) (\d+)',r'\1\2\3',str1) # \1\2\3 表示分组顺序
result_03 = re.sub('(\d+)\s+(\d+) (\d+)',r'\1\3\2',str1)# \1\2\3 表示分组顺序
result_04 = re.sub('(\d+)\s+(\d+) (\d+)',r'111',str1)# 匹配的替换为111
print(result_02)
print(result_03)
print(result_04)
result_05 = re.sub('\s,.*$','',str1)
print(result_05)


