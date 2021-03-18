import requests
from bs4 import BeautifulSoup
import csv
HOST = 'http://minfin.com.ua/'  
URL = 'http://minfin.com.ua/cards'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='itemlist')
    cards = []
    for item in items:
        cards.append(
            {
                'itemlist': item.find('div', class_='itemlist').get_text(strip=True),
                'link_prodact': HOST + item.find('div', class_='itemlist').find('a').get('href'),
                'brand': item.find('div', class_='brand').get_text(strip=True),
                'cars_img': HOST + item.find('div', class_='image').find('img').get('src')
            }
        )

    return cards

def parser():
    PAGENATION = input('страниц для парсинга:')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print('Error')


