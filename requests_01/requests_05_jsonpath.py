import jsonpath
import json
import re
# jsonpath 模块  json提取器
# json_obj ={'name':'小红','age':'18'}
# print(json_obj['name']) # 提取name
# print(json_obj.get('name'))# 提取name
#
# # value = jsonpath.jsonpath(json_obj,'$.name') 取出来是['小红']
# value = jsonpath.jsonpath(json_obj,'$.name')[0]
# print(value)
#
# # jsonpath语法规则  jsonpath.jsonpath（json对象，jsonpath表达式）
# json_obj_01 ={"tage":[{"id":"2","name":"王大大","ss":"11"},{"id":"21","name":"王大大1","ss":"111"}]}
# value01 = jsonpath.jsonpath(json_obj_01,'$.tage[*].name')
# print(value01)
#

# c = {"id":130,"name":"茅台人6"}
# d = json.dumps(c,ensure_ascii=False)
# print(d)
# value10 = jsonpath.jsonpath(c,'$.id')[0]
# print(value10)

a = {"tag":{"id":130,"name":"茅台人6"}}
b  = a.values()
print(b)
for i in b :
    print(i)
    c = i.values()
    print(c)
    for l in c :
        print(l)
        # d = l[0]
        # print(d)


# csrf_token_info = re.findall(''id': (.+?),',b)[0]



