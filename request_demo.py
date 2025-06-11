"""
'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history',
'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status',
 'raw', 'reason', 'request', 'status_code', 'text', 'url'
"""



import requests
import json

url = 'https://api.restful-api.dev/objects'

d = json.dumps({
    "id": 50,
   "name": "RealmeXT",
   "data": {
      "year": 2225,
      "price": 4444.99,
      "CPU model": "Intel Core i11",
      "Hard disk size": "64 GB"
   }
})

# # POST
rp = requests.post(url, data=d, headers= {"content-type": "application/json"})
print(rp.content)

# rp = requests.put(url, data=dp, headers={"content-type": "application/json"})
# print(rp.content)

# created obj ID : ff80818196f2a23f01975efd41c8682e

# r = requests.get(url)
# print(r.text)





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









