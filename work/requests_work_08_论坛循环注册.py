# 3、用 charles+requests 完成论坛的注册。
import requests
import re

# 论坛地址  http://47.107.178.45/phpwind/index.php
# 获取  csrf_token--->name="csrf_token" value="e395939fb229343f"/>
hosts = '47.107.178.45'
session = requests.session()
for i in range(4,10):
    response = session.get(url = 'http://%s/phpwind/index.php'%hosts)
    body = response.content.decode('utf-8')
    csrf_token_info = re.findall('name="csrf_token" value="(.+?)"/>',body)[0]
    print(csrf_token_info)

    # 注册接口  http://47.107.178.45/phpwind/index.php?m=u&c=register&a=dorun
    param_info = {"m":"u","c":"register","a":"dorun"}
    header_info = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
                   "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Accept-Language":"zh-CN,zh;q=0.9"
                   }

    user_info ={"username":'wyp0%d'%i,
                "password":"123456",
                "repassword":"123456",
                "email":"3%d5757028@qq.com"%i,
                "csrf_token":csrf_token_info}
    response01 = session.post(url = 'http://%s/phpwind/index.php'%hosts,
                              params = param_info,
                              headers = header_info,
                              data = user_info,
                              verify = False
                              )
    body01 = response01.content.decode('utf-8')
    print(body01)
    # username_body = re.findall('<h1>(.+?)，恭喜您注册成为phpwind 9.0会员！</h1>')
    # if username_body == username:
    #     print(username,'恭喜您注册成为phpwind 9.0会员！')
    # else:
    #     print(username,'注册失败')