#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re_demoo01.py
# @time: 2021/3/28 9:19
import re

str1 = 'hello123hello'
str2 = '''hello123hello
hello1hello
'''
result = re.match('\d+hello',str1) # match 匹配开头，从最左方开始匹配
print(result)
# 匹配两项
result1 = re.match('hello[\d,\D]+o',str2) # match 匹配开头，从最左方开始匹配
print(result1.group())
# 匹配一项
# result = re.match('hello\d+h',str2) # match 匹配开头，从最左方开始匹配
# print(result.group())

# ()分组 用group(1) 可以取具体那一组
str3 = '''newdream come on!
newdream come good!
 '''
# result2 = re.match('.+ .+ .+',str3)
# print(result2.group())
# result3 = re.match('(.+) (.+) (.+)',str3)
# print(result3.group(1))
# print(result3.group(2))
# print(result3.group(3))
# print(result3.group(1,2,3))
result4 = re.match('(.+) Come (.+)!\s',str3,re.I)
print(result4.group())
