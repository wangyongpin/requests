# 1、用 requests 完成 微信公众平台创建标签的请求，要求创建 标签名为  大学生组 。保证不乱码；
import  requests
import re
import json
import jsonpath

# 1、获取token  在修改标签，修改标签为中文是需要转为为utf-8  # ensure_ascii把udcode编码转换为中文
# 获取token https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
session = requests.session()
params_info={'grant_typ'
             'e':'client_credential',
             'appid': 'wx6615c989f6af590d',
             'secret': 'adfaa8d02c1301165613dde618bbbba0'
             }
response = session.get(url = 'https://api.weixin.qq.com/cgi-bin/token',
                        params = params_info,
                        verify = False)
r_str = response.content.decode('utf-8')
r_json = json.loads(r_str) # 把一个字符串转换为json对象------------解决乱码
value = jsonpath.jsonpath(r_json,'$.access_token')[0] # 获取--------jsonpath.jsonpath获取access_token
print(value)

# 新建标签  https://api.weixin.qq.com/cgi-bin/tags/create?access_token=ACCESS_TOKEN
data_info = {  "tag" : { "name" : "大学生组" } }
tooken_info = {"access_token":value}
josn_str = json.dumps(data_info,ensure_ascii=False) # 把一个json转换成一个字符串
response01 = session.post(url = 'https://api.weixin.qq.com/cgi-bin/tags/create',
                           data= josn_str.encode('utf-8)'), # 字符转utf-8格式，换为data------------解决乱码
                           params = tooken_info,
                           verify = False)
print(response01.content.decode('utf-8'))
