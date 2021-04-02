# 业务知识
# 1、https://mp.weixin.qq.com/ 2、订阅号--开发设计文档 3、获取access_tonken
# access_tonken 是公众号的全局唯一接口调用凭证
# appID   wx6615c989f6af590d
# appsecret   adfaa8d02c1301165613dde618bbbba0

# GET
#  https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
# HTTPS 协议类型
# api.weixin.qq.com 主机地址
# /cgi-bin/token 请求地址
# grant_type=client_credential&appid=APPID&secret=APPSECRET   接口的URL参数
# 参数直接用 & 进行分割的

import requests
import json
import jsonpath
# 方式一：  带参数的接口请求
# response = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx6615c989f6af590d&secret=adfaa8d02c1301165613dde618bbbba0')
# print(response.content.decode('utf-8'))

# 方式二:
url_params = {"grant_type":"client_credential",
              "appid":"wx6615c989f6af590d",
              "secret":"adfaa8d02c1301165613dde618bbbba0"
              }

response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                        params = url_params, # params 的参数值就可以是 字典类型的URL 参数
                        verify = False)
# print(response.content.decode('utf-8'))

body_str = response.content.decode('utf-8')
print(body_str)
body_obj = json.loads(body_str)   # 把一个字符串转换为json对象
print(body_obj)
value = jsonpath.jsonpath(body_obj,'$.access_token')[0]
print(value)

# 向服务器提交json格式数据的时候，可以在请求头部添加 conten-type= application/json
