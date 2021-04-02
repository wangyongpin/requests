
# unittest 中的testloader 测试用例加载器
# 方式一: discover  方法 自动遍历目录加载用例
import unittest
import os,time
import HTMLTestRunner
case_path = os.path.dirname(__file__) # 当前路径
report_path = os.path.join(case_path,'..//report') # 输入位置
print(case_path)
discover = unittest.defaultTestLoader.discover(start_dir = case_path,
                                               pattern='requests*.py')
suit = unittest.TestSuite()
suit.addTest(discover)
# unittest.main(verbosity=2,defaultTest='suit')


html_path = os.path.join(report_path,'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))
file = open(html_path,'wb',encoding='utf-8')
html_runner =  HTMLTestRunner.HTMLTestRunner( stream=file,
                                              title='requests接口测试',
                                              description='由接口自动化测试完成，包含大部分'
                                            )
html_runner.run(suit)
file.close()


