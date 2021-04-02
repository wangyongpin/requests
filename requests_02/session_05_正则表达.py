 # 论坛登陆抓包 上一个请求返回的数据部分。是必须用 给下一个请求 token
# http://192.168.1.102/phpwind/index.php 论坛地址
# 在requests中每个请求都是独立存在的
# 在在requests 中的seesion 是保持所有请求连起来
# 总结以后登陆之后的操作不是一个请求能完成的，都需要用到session连起来，先创建一个session对象
import requests
import re # python 处理 正则表达式的内置模块

session3 = requests.session() # 创建session对象
response01 = session3.get(url = 'http://192.168.1.102/phpwind') # 打开登陆
body = response01.content.decode('utf-8')
vauel = re.findall('name="csrf_token" value="(.+?)"/>',body)[0] # 获取token
print(vauel)

 #  输入账号密码登陆
url_param_info ={"m":"u","c":"login","a":"dologin"}
user_info = {
    'username':"admin",
    "password":"123456",
    "csrf_token":vauel
}
header_dict = {"Accept":"application/json, text/javascript, */*; q=0.01",
               "X-Requested-With":"XMLHttpRequest",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}
response02 = session3.post(url = 'http://192.168.1.102/phpwind/index.php',
                          headers = header_dict,
                          params = url_param_info,
                          data = user_info) # fromdata == data
print(response02.json())



