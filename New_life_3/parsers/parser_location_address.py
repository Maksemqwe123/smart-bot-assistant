from bs4 import BeautifulSoup
import requests

loc_address_cinema = []

url = 'https://www.relax.by/cat/ent/kino/gomel/'

response = requests.get(url=url)

pages_info = BeautifulSoup(response.text, 'html.parser')

address_cinema = pages_info.find_all('span', class_='Place__addressText')
for i in address_cinema:
    loc_address_cinema.append(i.text)
