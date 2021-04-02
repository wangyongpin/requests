#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re.demo_07subn.py
# @time: 2021/3/28 11:00
import re
str1 = '''newdream come on!!
google come on!!
'''
value = re.subn('(\w+) (\w+) (\w+)',r'\2 \3 \1',str1)
print(type(value))
print(value)
