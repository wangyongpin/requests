import requests

# 添加cookie
# 方式一
cookie_dic = {'Cookie':'like=wdd'}
rsposne = requests.get(url ='http://192.168.1.102/phpwind',
                       cookies = cookie_dic)
# 方式二
header_info = {'Cookie':'like=wdd'}
rsposne1 = requests.get(url ='http://192.168.1.102/phpwind',
                       deaders = cookie_dic)

# 方式三 3.1
# session = requests.session()
# session.cookies['like']= 'wangdada'
# session.cookies['name']= 'session添加cookie'
# session= requests.get(url ='http://192.168.1.102/phpwind')

# 方式三3.2
# session = requests.session()
# session.cookies.set('like','newdream',path='/')
# session.get(url ='http://192.168.1.102/phpwind')

# 方式三3.3
# session = requests.session()
# cookie_dic = {'like':'wangdada'}
# requests.utils.add_dict_to_cookiejar(session.cookies,cookie_dic)
# session.get(url ='http://192.168.1.102/phpwind')

# 方式三3.4
# session = requests.session()
# cookies_obj = requests.cookies.RequestsCookidJar()
# cookies_obj.set('like','newdeam',domain='192.168.1.102',path='/')
# session.cookies.update(cookies_obj)
# session.get(url ='http://192.168.1.102/phpwind' )







