from api.api_get_data import getter
import requests

# class unit_list(object):
#     pass
url = 'http://192.168.30.11:10060/supervisor/admin/sysadmin/login'
headers = {'Content-Type': 'application/json;charset=UTF-8'}
json = {"password": "admin", "phone": "admin", "rememberMe": True}
s = requests.session()
resp = s.post(url=url, headers=headers, json=json)
# print(response.json())
token, userId = resp.json()['data']['token'], resp.json()['data']['sysAdmin']['id']

url2 = 'http://192.168.30.11:10060/supervisor/unit/list'
json2 = {"pageNum": "1", "pageSize": "10", "token": token, "userid": userId}
resp2 = s.post(url=url2,headers=headers,json=json2)
print(resp2.json())
