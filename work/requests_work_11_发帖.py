# requests 模拟网站业务操作步骤
# 1、开启charles抓包，把需要完成的业务请求操作斌在charles进行模拟进行hosts备注
# 2、利用requests进行charles进行模拟
# 3、脚本调试，3.1参数值如果是动态字符串时候，基本上是要关联
# 3.3 脚本调试不成功，吧请求头，请求行，请求正文进行真是和模拟的对比，检查对比
from collections import OrderedDict

import requests
import re
# http://192.168.1.102/phpwind/
proxy_server = {"http":"http://127.0.0.1:8888"}
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
                          headers = header_info,
                          proxies = proxy_server
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
                         params = url_params_info,
                         proxies=proxy_server
                         )
# 进入接口测试板块
url_params = {
"c":"post",
"fid":"5"
}
response03 = session.get(url = 'http://192.168.1.102/phpwind/index.php',
                         params = url_params,
                         proxies=proxy_server
                         )
# 进入发帖界面
# url_params = {
#
# }

# 方法一发帖请求
'''
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
                          data = data_params,
                          proxies=proxy_server
                        )

res = response04.content.decode('utf-8')
print(res)
'''
# 方法二  发帖
form_data = OrderedDict(
    [
        ("atc_title",(None,'P3P4002')),
       ("atc_content",(None,'P3P4004')),
        ("pid",(None,'')),
        ("tid",(None,'')),
        ("special",(None,'default')),
        ("reply_notice",(None,'1')),
        ("csrf_token",(None,token))
    ]
)
response = session.post(url="http://%s/phpwind/index.php"%hosts,
                    params=url_params,
                    files=form_data)
print( response.content.decode('utf-8') )

# 方式三
'''
class MultipartFormData(object):
    """multipart/form-data格式转化"""

    @staticmethod
    def format(data, boundary="----WebKitFormBoundary4P1UZZFFTebimczJ", headers={}):
        """
        form data
        :param: data:  {"req":{"cno":"18990876","flag":"Y"},"ts":1,"sig":1,"v": 2.0}
        :param: boundary: "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        :param: headers: 包含boundary的头信息；如果boundary与headers同时存在以headers为准
        :return: str
        :rtype: str
        """
        # 从headers中提取boundary信息
        if "content-type" in headers:
            fd_val = str(headers["content-type"])
            if "boundary" in fd_val:
                fd_val = fd_val.split(";")[1].strip()
                boundary = fd_val.split("=")[1].strip()
            else:
                raise Exception("multipart/form-data头信息错误，请检查content-type key是否包含boundary")
        # form-data格式定式
        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'
        end_str = "--{}--".format(boundary)
        args_str = ""

        if not isinstance(data, dict):
            raise Exception("multipart/form-data参数错误，data参数应为dict类型")
        for key, value in data.items():
            args_str = args_str + jion_str.format(boundary, key, value)

        args_str = args_str + end_str.format(boundary)
        args_str = args_str.replace("\'", "\"")
        return args_str

headerinfos_01 = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Content-Type':'multipart/form-data;boundary=------WebKitFormBoundary4P1UZZFFTebimczJ'
}

get_params_03 = {
    "c":"post",
    "a":"doadd",
    "_json":"1",
    "fid":"80"
}

form_data = {
    'atc_title':'new001',
    'atc_content':'new001',
    'pid':'',
    'tid':'',
    'special':'default',
    'reply_notice':'1',
    'csrf_token':token
}

m_data = MultipartFormData.format(data=form_data, headers=headerinfos_01)

response04 = session_req.post( url='http://47.107.178.45/phpwind/index.php', #登录
                              params = get_params_03,
                              headers = headerinfos_01,
                              data=m_data
                              )
print( response04.content.decode('utf-8') )
'''