#дз olx

from math import hypot

import requests
from bs4 import BeautifulSoup

Category = 'house'
Language = '/uzb/'
Url = 'https://www.olx.uz/d/obyavlenie/kvartira-mehmonxona-xostel-hotel-kunlik-ijara-ID3XQRj.html?reason=hp%7Cpromoted'
Host = Url+Language+Category
Header = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(Url, headers = Header).text

soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('div', class_='article')
DATA = []

for article in articles:
    title = article.find('div' , class_='nt').find('h3').get_text(strip=True)
    print(title)