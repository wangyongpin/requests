import requests

reponse = requests.get( url = 'http://www.hnxmxit.com')
print(reponse.status_code) # 获取状态吗
print(reponse.reason) # 获取 响应信息
print(reponse.headers) # 获取 头部信息
print(reponse.headers.get('content-type')) # 获取 对应的值
print(reponse.url) # 获取 URL
print(reponse.cookies) # 获取cookies
print(reponse.encoding) # 获取 编码

# 1、获取 内容文本
# print(reponse.text)
# 2、获取 内容文本  解码
# print(reponse.content.decode('utf-8'))

# 、 响应正文为图片  安装pillow
from PIL import Image
from io import BytesIO
respones_img = requests.get(url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1603365312,3218205429&fm=26&gp=0.jpg')
img_obj = Image.opne(BytesIO(respones_img.content))
img_obj.save('test.png')

# 3、 返回的是json 格式
# reponse1 = requests.get( url = 'http://www.hnxmxit.com')
# body = reponse1.json()
# print(body)
#
# # 4、原始响应
# reponse2 = requests.get( url = 'http://www.hnxmxit.com',stream=True)
# print(reponse2.raw.read(3)) # 表示获取前三个





