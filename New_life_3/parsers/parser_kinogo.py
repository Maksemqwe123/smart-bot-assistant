from bs4 import BeautifulSoup
import requests

kinogo_urls = []
kinogo_decription = []


def film_kinogo():
    url = f'https://kinogo.film/films-2021/'

    response = requests.get(url=url)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    films = pages_info.find_all('div', class_='shortstory')

    for film in films:
        urls = film.find('h2', class_='zagolovki').find('a').get('href')
        description = film.find('h2', class_='zagolovki').find('a').text

        kinogo_urls.append(urls)
        kinogo_decription.append(description)
    return kinogo_urls, kinogo_decription


parser_kinogo = film_kinogo()

all_kinogo = list(zip(kinogo_decription, kinogo_urls))
kinogo_no_duplicates = list(set(all_kinogo))
