import requests
from bs4 import BeautifulSoup

URL = 'https://neptun66.ru/search/index.php?q=Galmet'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'accept': '*/*'}
HOST = 'https://neptun66.ru'

def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_='catalog-item')

	products = []
	for item in items:
		products.append({
			'title': item.find('a', class_='js-prodname').get_text(),
			'link': HOST + item.find('a', class_='js-prodname').get('href'),
			'price': item.find('price', class_='js-price').get_text(),
			# 'product_code': item.find('p').get_text(strip=True).replace("Артикул:", "")
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
