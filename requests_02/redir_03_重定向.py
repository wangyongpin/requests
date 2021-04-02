# 重定向 是指返回的是3**

import requests
# http://www.360buy.com ==金东的老网站
# allow_redirects=False  设置后表示不用重定向
respones = requests.get('http://www.360buy.com',allow_redirects=False)
print(respones.history)
print(respones.url)
print(respones.content.decode('utf-8'))