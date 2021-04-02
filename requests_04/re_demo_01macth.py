#!/usr/bin/env python
# encoding: utf-8
# @authot: wdd
# @file:re_demo.py
# @time: 2021/3/28 8:57

# 正则表达式
import re
str1 = 'newdream'
str2 = '''hello12h
12hello
hello1235ho'''
# 方式一
   #创建正则规则
pattern_01 = re.compile(r'n\w+m') # 正则规则
resuit_01 = re.match(pattern_01,str1) # 运用正则规则
print(resuit_01.group())

pattern_02 = re.compile(r'hello\d+h') # 正则规则
resuit_02 = re.findall(pattern_02,str2) # 运用正则规则
print(resuit_02)

# 方式二
  #  直接用函数匹配
resuit_03 = re.match('n\w+m',str1)
print(resuit_03.group())

#　方式三
resuit_0４ = pattern_01.match(str1)
print(resuit_0４.group())


'''
.匹配任意除换行符"\n"外的字符
+匹配前一个字符1次或无限次
?匹配一个字符0次或1次，还有一个功能是可以防止贪婪匹配
^匹配字符串开头
$  匹配字符串末尾
｜ 匹配该符合两边的一个
() 匹配括号内的表达式，也表示一个组
[] 匹配字符组中的字符
[^] 匹配除了字符组中字符的所有字符
{n}重复n次
{n,}重复n次或更多次
{n,m}重复n到m次
'''
'''
2、预定义字符集表
\d匹配数字
\D匹配非数字
\w匹配字母或数字或下划线
\W匹配非字母或数字或下划线
\s匹配任意的空白符
\S匹配非空白符
\n匹配一个换行符
\t匹配一个制表符
\A仅匹配字符串开头,同^
\Z仅匹配字符串结尾，同$
\b匹配一个单词边界，也就是指单词和空格间的位置
'''