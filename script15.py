#дз parser

from math import hypot

import requests
from bs4 import BeautifulSoup

category = 'Elektronika'
language = 'uzb/'
url = 'https://uzum.uz/uz/product/xiaomi-redmi-note-3272157?skuId=12071190'

host = category + language + url
print(host)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 Edg/154.0.0.0'}

html = requests.get(url, headers=header)

soup = BeautifulSoup('html', 'html.parser')
articles = soup.find_all('div', class_='article')
Data = []


for article in articles:
    title = article.find('div', class_='nt').find('h3').get_text(strip=True)
    article = url + article.find('div', class_='nt').find('a').find('h3').get['href']
    print(article_link)