
# post 文件上传
import requests
# 处理方式一
exec_file_obj = open('requests_test.xlsx','rb')
# excel_file_data = {'file',exec_file_obj}
# 处理方式二：
excel_file_data = {'file':('requests_test',exec_file_obj,'application/vnd.ms-excel')}
respose = requests.post( url = 'http://httpbin.org/posg',
                          files = excel_file_data)  # 上传文件

print(respose.content.decode('utf-8'))