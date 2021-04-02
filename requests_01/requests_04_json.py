#  json模块
# python中的字典类型的数据格式是json格式数据
# json模块是python内置的模块

import  json
json_obk ={'name':'小红','age':'18'}
#  ensure_ascii把udcode编码转换为中文
josn_str = json.dumps(json_obk,ensure_ascii=False) # 吧一个json转换成一个字符串
print( type(josn_str))
print(josn_str)

str_01 = '{"book_name":"哈哈","price":14.8}'
json_obj = json.loads((str_01)) # 把一个字符串转换为json对象
print( type(json_obj))
print(json_obj)


# 修改用户标签
import  requests
import json
 # https://api.weixin.qq.com/cgi-bin/tags/update?access_token=ACCESS_TOKEN
url_params = {"access_token":"42_ooH7FKN36Q0uG-ptg6t1ayY5xjmUj2gXgP_Xmazb0Yx4ZVeyKOCbb33oesEOubNsbsFyHWWa3kVUW2ZcCIusR0QWZ_H6C4G7PIq2PyLGwezmeMU95lL5uog2HuGVelEEHbfc4LQRMKA4srwxRPOgAIAUSR"
}
# header_info = {'conten-type':'application/json'}
tag_info = {"tag" : {"id" : 118,"name" : "茅台人" } }
json_str =json.dumps(tag_info,ensure_ascii=False) # ensure_ascii把udcode编码转换为中文
print(json_str)
response = requests.post( url = 'https://api.weixin.qq.com/cgi-bin/tags/update',
                          params = url_params,
                          # headers = header_info,
                          data= json_str.encode('utf-8)'))
                          # json = tag_info ) # json 代表传输POST为json格式的数据
print(response.content.decode('utf-8'))


