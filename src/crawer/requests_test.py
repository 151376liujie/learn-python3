from http.client import responses

import requests

link = r'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
params = {
    'key1': 'value1',
    'key2': 'value2'
}

link = r'http://httpbin.org/post'
# response = requests.get(link, headers=headers, params=params)
response = requests.post(link, data=params)
print(response.json())
# print(response.content)