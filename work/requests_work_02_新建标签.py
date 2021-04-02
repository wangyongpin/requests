# 使用 requests 模拟 获取 access_token、添加用户标签、修改用户标签、删除用户标签 的请求
  # 添加用户标签
import  requests

url_params = {"access_token":"42_ooH7FKN36Q0uG-ptg6t1ayY5xjmUj2gXgP_Xmazb0Yx4ZVeyKOCbb33oesEOubNsbsFyHWWa3kVUW2ZcCIusR0QWZ_H6C4G7PIq2PyLGwezmeMU95lL5uog2HuGVelEEHbfc4LQRMKA4srwxRPOgAIAUSR"
}
tag_info = {"tag" : { "name":"上海1" } }

response = requests.post( url = ' https://api.weixin.qq.com/cgi-bin/tags/create',
                          params = url_params,
                          json = tag_info ) # json 代表传输POST为json格式的数据

print(response.content.decode('utf-8'))