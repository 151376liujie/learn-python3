import requests
from bs4 import BeautifulSoup

"""
《python网络爬虫从入门到实践》一书中的爬虫
"""

link = r'http://www.santostang.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

response = requests.get(link, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
for item in soup.find_all('h1', class_='post-title'):
    print(item.a.text)
