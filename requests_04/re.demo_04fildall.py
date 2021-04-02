#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re.demo_04fildall.py
# @time: 2021/3/28 9:51

# findall() 查找所有  并返回迭代器
import re

str1 = 'hello 123 hello'
result_01 = re.search('\w+',str1)
result_02 = re.findall('\w+',str1)
patten_01 = re.compile('\w+')
result_03 = patten_01.findall(str1,pos=5,endpos=12)
print(result_01.group())
print(result_02)
print(result_03)

for i in result_03:
    print(i)
