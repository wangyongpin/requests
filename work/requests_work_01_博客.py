import requests
header_info ={
        # "upgrade-insecure-requests":"1",
        # "sec-fetch-user":"?1",
        # "sec-fetch-site":"none",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate, br",
        # "accept-language":"zh-CN,zh;q=0.9"
        }
respones = requests.get( url = 'https://www.cnblogs.com/',
                         headers = header_info,
                         verify = False)
print(respones.content.decode('utf-8'))
print(respones.headers)