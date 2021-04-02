#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re.demo_03.py
# @time: 2021/3/28 9:44

# search函数 全字符查找找到第一个就停止
import re
str1 = 'nEwDreamEaaaa'
pattern_o1 = re.compile('e\w',re.IGNORECASE)
result_01 = re.search(pattern_o1,str1)
print(result_01.group())

result_02 = re.search('e\w',str1,re.I)
print(result_02.group())