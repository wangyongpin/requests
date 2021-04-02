# 如何使用unittest
import unittest  # 1、导入unittest
import requests
import jsonpath
import json

class TestRequestsDemo(unittest.TestCase): # 2、编写一个类继承TestCase类
    # 3、fixtrue 配置代码
    def setUp(self) -> None:
        self.hosts = 'api.weixin.qq.com'
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()
# 默认执行顺序：测试方法名称字符串根据acsii逐位比对，小的先执行
    def test_02_get(self):
        # 断言
        self.assertEqual(1,1)
# 不执行
    @unittest.skip('不想执行')
    def test_03_get(self):
        self.assertEqual(1, 1)

    def test_01_get_access_token_api(self):  # 4.编写测试方法 == 编写测试用例
        # 微信获取token
        url_params = {
            "grant_type": "client_credential",
            "appid": "wx55614004f367f8ca",
            "secret": "65515b46dd758dfdb09420bb7db2c67f"
        }
        response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
                                    params = url_params)
        json_obj = response.json()
        actual_result = jsonpath.jsonpath( json_obj,'$.expires_in' )[0]
        print(actual_result)
        self.assertEqual(actual_result,7200)  # 一定要写断言语句
        body_str = response.content.decode('utf-8')
        body_obj = json.loads(body_str)  # 把一个字符串转换为json对象
        token = jsonpath.jsonpath(body_obj, '$.access_token')[0]
        print(token)
if __name__ == '__main__':
    unittest.main(verbosity=2)  # 5、执行测试用例代码
# #   手动改变顺序
# suite = unittest.TestSuite()
# suite.addTest(TestRequestsDemo('test_02_get'))
# suite.addTest(TestRequestsDemo('test_01_get_access_token_api'))
# unittest.main(verbosity=2,defaultTest='suite')