import requests
from bs4 import BeautifulSoup

URL = 'https://www.taen.ru/brands/galmet/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.taen.ru'

def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='con-box')

	products = []
	for item in items:
		products.append({
			'title': item.find('a').get_text(strip=True),
			'link': HOST + item.find('a').get('href'),
			'price': item.find('span', class_='co-price').get_text().replace("р.", "").replace(" ", ""),
			'product_code': item.find('p').get_text(strip=True).replace("Артикул:", "")
		})

	print(products)
	# return products

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		products = get_content(html.text)
	else:
		print('Error')


parse()
