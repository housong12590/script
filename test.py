import requests
import json

session = requests.session()

login_url = 'https://proxy.jiankanghao.net/login'

login_data = {
    'username': 'haiwei',
    'password': 'CvC9rjhTB3wTcFju'
}

login_data = json.dumps(login_data)
headers = {'contentType': 'application/json; charset=utf-8'}

resp = session.post(login_url, data=login_data, headers=headers)
if resp.status_code == 200:
    resp = json.loads(resp.text)
else:
    raise Exception('---------登录失败----------')

detail_url = 'https://proxy.jiankanghao.net/config/detail'

requests.utils.add_dict_to_cookiejar(session.cookies, {'token': resp.get('data')})
resp = session.post(detail_url)


def add(data):
    add_url = 'https://proxy.jiankanghao.net/config/update'
    data = json.dumps(data)
    r = session.post(add_url, data)
    print(r.text)


if resp.status_code == 200:
    resp = json.loads(resp.text)
    if resp.get('code') == 20000:
        client_list = resp.get('data')
        try:
            client_list[2]['proxyMappings'].append({
                'name': 'ops',
                'inetPort': '55032',
                'lan': '127.0.0.1:455'
            })
            add(client_list)
        except Exception as e:
            print(e)
