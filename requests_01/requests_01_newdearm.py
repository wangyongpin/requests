# import  requests
# requests 模拟请求头信息 搜索newdearm
# header_info ={
#             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
#             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'Accept-Encoding':'gzip, deflate, br'
# }
# response = requests.get( url ='https://www.baidu.com/s?wd=newdream',
#                          headers = header_info,
#                          verify = False)
# print(response.content.decode('utf-8'))

# 搜索 天天向上
# import  requests
# header_info ={
#             'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'Accept-Encoding':'gzip, deflate, br'
# }
# response = requests.get( url ='http://www.baidu.com/s?wd=天天向上',
#                          headers = header_info,
#                          verify = False)
# print(response.content.decode('utf-8'))


# 百度搜索12306
import  requests
header_info ={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding':'gzip, deflate, br'
}
response = requests.get( url ='http://www.baidu.com/s?wd=12306',
                         headers = header_info,
                         verify = False)
print(response.content.decode('utf-8'))





