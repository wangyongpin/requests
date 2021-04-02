import requests
 # 解决返回text 乱码问题
response =requests.get(url='http://www.baidu.com')
print(response.encoding) # ISO-8859-1
print(response.headers)  #'Content-Encoding': 'gzip',　　格式
# requests通过响应中的 Content-Encoding Content_type 进行编码的推测gzip==》 ISO-8859-1
  # 解决方法 1
# response.encoding='utf-8'
# print(response.text) # 可能出现乱码
 # 解决方法 2 推荐使用
print(response.apparent_encoding) # 根据网页的正文预测网页的编码
response.encoding = response.apparent_encoding # 自动解决响应乱码的问题
print(response.text)



