import requests
import re
# http://192.168.1.102/phpwind/
hosts = '192.168.1.102'
session = requests.session()
# ------打开首页
response = session.get(url = 'http://%s/phpwind/'%hosts)
body = response.content.decode('utf-8')
token = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]
print(token)
# ------登陆
url_param_info = {
        "m":"u",
        "c":"login",
        "a":"dologin"
    }
user_info = {
        "username":"admin",
        "password":"123456",
        "csrf_token":token
}
header_info = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9"
    }
response01 = session.post(url = 'http://%s/phpwind/index.php'%hosts,
                          params = url_param_info,
                          data = user_info,
                          headers = header_info
                          )
body01 = response01.content.decode('utf-8')
statu = re.findall('_statu(.+?)"',body01)[0]
print(statu)
# ------登陆成功后跳转
url_params_info = {
    "m":"u",
    "c":"login",
    "a":"welcome",
    "_statu":statu
}
response02 = session.get(url = 'http://%s/phpwind/index.php'%hosts,
                         params = url_params_info )
# ------回复帖子
url_params_info1 = {
    "c":"post",
    "a":"doreply",
    "_getHtml":1
}
date_info ={
    "csrf_token":token,
    "atc_content":"接口回复的帖子哈哈哈哈2021032213",
    "tid":32
    }
# header1_info ={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#     "Accept-Language":"zh-CN,zh;q=0.9"
# }

response03 = session.post(url = 'http://%s/phpwind/index.php'%hosts,
                          params = url_params_info1,
                          data = date_info
                          )
seccuss = response03.content.decode('utf-8')
# 回帖后跳转
url_params = { "m":"u",
                "a":"showcredit"

    }

data_body = {"csrf_token":token
}

response01 = session.post(url = 'http://47.107.178.45/phpwind/index.php',
                        params = url_params,
                        headers = data_body
                        )
print(response01.content.decode('utf-8'))
print('结束了')



