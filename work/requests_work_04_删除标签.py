# 删除用户标签

import  requests
url_params = {"access_token":"42_94t222KlVxd6RKTsaem_kcktFLxZvaK04DISzuwk_iXRTHseBmFM5j1_4E1kQORqh08f97SSPIXLDH4o3xelRkdctcqGlds3uLCOoLy5eLsvcfvYC9zQYh34xmb363xxvAVdEHmJEasMTR87VFKhAHAYIN"
}
tag_info = { "tag":{ "id" : 117 } }
response = requests.post( url = 'https://api.weixin.qq.com/cgi-bin/tags/delete',
                          params = url_params,
                          json = tag_info ) # json 代表传输POST为json格式的数据

print(response.content.decode('utf-8'))