 # 对请求设定时限 1、特殊需求 请求必须在3秒返回。 3秒至后返回的没用==》多个服务器 一个大系统 心跳包
import requests
# response = requests.get(url='http://baidu.com',timeout=0.1) #  float 单位为妙 代表数据链接超时时间
# print(response.content.decode('utf-8'))

# response = requests.get(url='http://baidu.com',timeout=(0.1,0.2)) # 0.1链接时间，0.2数据接收响应时间
# print(response.content.decode('utf-8'))

response = requests.get(url='http://baidu.com',timeout=None) # None 直到服务器返回数据为止
print(response.content.decode('utf-8'))
