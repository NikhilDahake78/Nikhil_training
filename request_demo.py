"""
'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history',
'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status',
 'raw', 'reason', 'request', 'status_code', 'text', 'url'
"""


import requests
import json
import re


url = 'https://api.restful-api.dev/objects'

d = json.dumps({
   "name": "RealmeXT",
   "data": {"year": 2020, "price": 500000}})


# # POST
r = requests.post(url, data=d, headers= {"content-type": "application/json"})
text = r.text
print('POST')
print(text)

print('Header')
print(r.headers)


print('\n')

id_n = re.findall(r'"id":"([a-z0-9]+)', text)
print(id_n)
print('\n')


# #GET
print('GET')
rg = requests.get(url+f"/{id_n[0]}")
print(rg.text)
print('\n')


# # PUT
print('PUT')
dp = json.dumps({
   "name": "RealmeXT",
   "data": {"year": 2019, "price": 44444}})
rp = requests.put(url+f"/{id_n[0]}", data=dp, headers={"content-type": "application/json"})
print(rp.text)
print('\n')



# # PATCH
print('PATCH')
rpp = requests.patch(url+f"/{id_n[0]}", data=json.dumps({"name":"RealmeXT new"}), headers={"content-type": "application/json"})
print(rpp.text)
print('\n')



# # DELETE
print('DELETE')
rd = requests.delete(url+f"/{id_n[0]}")
print(rd.status_code)






# ----------------------------------------------------------------------------------------


# r = requests.get('https://api.restful-api.dev/objects')
# print(r.text)

# https://www.api-basketball.com/
# r = requests.get('https://www.api-basketball.com/public/img/home1/hero-banner1.png')

# # wb : write byte
# with open('basket_banner.png', 'wb') as image:
#     image.write(r.content)

# print(type(r.content))  #<class 'bytes'>
# print(type(r.text))  #<class 'str'>
# print(r.text)

# payload = {'username': 'Harsh', 'Age': 44}
# r = requests.post("https://httpbin.org/post", data=payload)

# Timeout
# r = requests.get('https://httpbin.org/delay/3', timeout=2)









