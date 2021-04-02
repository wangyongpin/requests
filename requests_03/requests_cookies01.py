# cookies  实战  cookies 缓存登陆信息等
# requests 模拟网站业务操作步骤
# 1、开启charles抓包，把需要完成的业务请求操作斌在charles进行模拟进行hosts备注
import requests
import re
# http://192.168.1.102/phpwind/
# proxy_server = {"http":"http://127.0.0.1:8888"}
hosts = '192.168.1.102'
session = requests.session()
# ------打开首页
response = session.get(url = 'http://%s/phpwind/'%hosts)
body = response.content.decode('utf-8')
token = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]
print(token)
# ------登陆
# url_param_info = {
#         "m":"u",
#         "c":"login",
#         "a":"dologin"
#     }
# user_info = {
#         "username":"admin",
#         "password":"123456",
#         "csrf_token":token
# }
# header_info = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Language": "zh-CN,zh;q=0.9"
#     }
# response01 = session.post(url = 'http://%s/phpwind/index.php'%hosts,
#                           params = url_param_info,
#                           data = user_info,
#                           headers = header_info
#
#                           )
# body01 = response01.content.decode('utf-8')
# statu = re.findall('_statu(.+?)"',body01)[0]
# print(statu)
# # ------登陆成功后跳转
# url_params_info = {
#     "m":"u",
#     "c":"login",
#     "a":"welcome",
#     "_statu":statu
# }
# response02 = session.get(url = 'http://%s/phpwind/index.php'%hosts,
#                          params = url_params_info
#
#                          )
# 进入接口测试板块
# url_params = {
# "c":"post",
# "fid":"5"
# }
# response03 = session.get(url = 'http://192.168.1.102/phpwind/index.php',
#                          params = url_params,
#
#                          )

session.cookies.set("_ac_app_ua","7d61fbf9f56718e8b8")
session.cookies.set("csrf_token",token)
session.cookies.set("zFb_winduser","%2Fpg5ojYfJtl7nDiYwJsNFUxRH%2BZ0B%2BEI6Q7oqVI1D%2FYNahff5w6pMg%3D%3D")
session.cookies.set("zFb_visitor","okTeu8r%2BF1G9jXfh6HtT8%2FNpRPWQu2TnIlTJ3vuPKD0lErCBX68PWl4VXqg%3D")
session.cookies.set("zFb_lastvisit","2427%091615682357%09%2Fphpwind%2Findex.php%3Fm%3Du%26a%3Dshowcredit")
# 方法一发帖请求
url_params = {
        "c":"post",
        "a":"doadd",
        "_json":"1",
        "fid":"5"
    }
data_params = {
        "atc_title":"接口自动化02",
        "atc_content":"接口自动化02内容主题",
        "pid":"",
        "tid":"",
        "special":"default",
        "reply_notice":"1",
        "csrf_token":token
    }
response04 = session.post(url = 'http://192.168.1.102/phpwind/index.php',
                          params = url_params,
                          data = data_params
                        )

res = response04.content.decode('utf-8')
print(res)
