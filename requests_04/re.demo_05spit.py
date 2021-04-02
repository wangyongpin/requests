#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re.demo_05spit.py
# @time: 2021/3/28
# split
import  re
str1 = '中国$韩国$泰国$英国'
print(str1.split('$'))

str2 = '中国1韩国2泰国3英国'
print(re.split('\d',str2,maxsplit=2)) # maxsplit 分割几次

str3 = '中国 韩国 泰国   英国'
print(re.split('\s+',str3)) # maxsplit 分割几次
