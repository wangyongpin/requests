import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException
# ConnectionError, RequestException Exception
 #孙子类 继承 儿子类 继承 主异常类
# 异常处理
# IndexError 基于 Exception的子类
'''
try:
    response = requests.get( url = 'https://www.223ddddd.com')
    print(response.status_code)
except ConnectionError as e: # 异常编写规则， 子类或者具体的异常类写在最顶层
    print('链接异常，网址错误，连接不上',e)
except RequestException as e:
    print('requests出错',e)
except Exception as e:
    print('系统出错，可能不是requests的原因')
'''
try:
    response1 = requests.get(url = 'http://www.baidu.com',timeout =0.01)
    print(response1.content.decode('utf-8'))
except ConnectionError as e:
    print('链接太慢的，在10ms不能返回')
except RequestException as e:
    print('出现异常，不清楚原因')



