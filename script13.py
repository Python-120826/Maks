#дз olx после этого скрипта вторая версия его

# from math import hypot
#
# import requests
# from bs4 import BeautifulSoup
#
# Category = 'hotel'
# Language = '/ru/'
# Url = 'https://www.olx.uz/d/obyavlenie/kvartira-mehmonxona-xostel-hotel-kunlik-ijara-ID3XQRj.html?reason=hp%7Cpromoted'
# Host = Url+Language+Category
# Header = {'User-Agent': 'Mozilla/5.0'}
# html = requests.get(Url, headers = Header).text
#
# soup = BeautifulSoup(html, 'html.parser')
# articles = soup.find_all('div', class_='article')
# DATA = []
#
# for article in articles:
#     title = article.find('div' , class_='nt').find('h3').get_text(strip=True)
#     article_link = Url + article_find('div ', class_='nt').find('a').find('h3').get['href']
#     print(title)
#     print(article_link)


#дз olx N2

from math import hypot

import requests
from bs4 import BeautifulSoup

Category = 'Хостел'
Language = 'uzb/'
Url = 'https://www.olx.uz/'
Host = Url + Category + Language
print(Host)
Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0'}

html = requests.get(Host, headers = Header).text

soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('div', class_ = 'article')
DATA = []

for article in articles:
    title = article_find('div' , class_ ='nt').find('h3').get_text(strip = True)
    article_link = Url + article_find('div' , class_='nt').find('a').find('h3').get['href']
    print(article_link)