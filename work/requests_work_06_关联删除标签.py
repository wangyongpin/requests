# 2、把获取token 和 删除标签 做成关联的形式，不需要复制token值可以直接进行传递 ，使用jsonpath完成；
import  requests
import re
import json
import jsonpath

# 1、获取token  在修改标签，修改标签为中文是需要转为为utf-8  # ensure_ascii把udcode编码转换为中文
# 获取token https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
session = requests.session()
params_info={'grant_type':'client_credential',
             'appid': 'wx6615c989f6af590d',
             'secret': 'adfaa8d02c1301165613dde618bbbba0'
             }
response = session.get(url = 'https://api.weixin.qq.com/cgi-bin/token',
                        params = params_info,
                        verify = False)
r_str = response.content.decode('utf-8')
r_json = json.loads(r_str)# 把一个字符串转换为json对象
value = jsonpath.jsonpath(r_json,'$.access_token')[0]
print(value)

# 删除标签  https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=ACCESS_TOKEN
data_info = { "tag":{ "id" : 116  } }
tooken_info = {"access_token":value}
response01 = session.post(url = 'https://api.weixin.qq.com/cgi-bin/tags/delete',
                           json= data_info,
                           params = tooken_info,
                           verify = False)
print(response01.content.decode('utf-8'))

