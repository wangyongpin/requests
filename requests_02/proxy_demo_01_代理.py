# 代理用途 1、爬虫限制ip 多个代理去抓取数据 2、境外项目链接VPN测试

import requests
proxy_server = {
    'http':'http://127.0.0.1:8888',
    'https':'http://127.0.0.1:8888'
    }
# vpn有账号密码
# proxy_server = {
#     'http':'http://user:password@127.0.0.1:8888'
#     }
response = requests.get(url='http://hnxmxit.com',
                        proxies = proxy_server)
print(response.status_code)
