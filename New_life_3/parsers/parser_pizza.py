from bs4 import BeautifulSoup
import requests

urls_pizza = []


def deals():
    url = f'https://ym1.by/akczii/'

    response = requests.get(url=url)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    pizza_all = pages_info.find_all('article')
    for pizza in pizza_all:
        urls = pizza.find('a').get('href')
        urls_pizza.append(urls)

    return urls_pizza


parser_pizza = deals()

all_parser_pizza = list(zip(urls_pizza))
