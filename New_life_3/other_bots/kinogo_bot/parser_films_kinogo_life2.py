import time
import requests
from bs4 import BeautifulSoup

start_time = time.time()

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72',
}

items = []
urls = []
spend = []

items_genre = []
urls_genre = []
spend_genre = []


class Parser:
    def __init__(self, pages: range):
        self.pages = pages
        self.items = items
        self.urls = urls

        self._get_html()

    def _get_html(self):
        for page in self.pages:
            if page == 1:
                url = 'https://kinogo.film/films-2021/'
            else:
                url = f'https://kinogo.film/films-2021/page/{page}/'

            response = requests.get(url=url)

            try:
                assert response.status_code == 200
                html_source = response.text
                self._get_info(html_source)
            except AssertionError as e:
                print(f'ERROR: {repr(e)}')
                print(response.status_code)

    def _get_info(self, html_source):
        pages_info = BeautifulSoup(html_source, 'html.parser')

        films_names = pages_info.find_all('h2', class_='zagolovki')
        for name in films_names:
            self.items.append(name.text)
            films_urls_kinogo = name.find('a').get('href')
            self.urls.append(films_urls_kinogo)


class ParserGenre:
    def __init__(self, pages_genre: range, name: list):
        self.pages_genre = pages_genre
        self.name = name
        self.items_genre = items_genre
        self.urls_genre = urls_genre

        self._get_html()

    def _get_html(self):
        for page in self.pages_genre:
            if page == 1:
                url = f'https://kinogo.film/{self.name}/'
            else:
                url = f'https://kinogo.film/{self.name}/page/{page}/'

            response = requests.get(url=url, headers=headers)

            try:
                assert response.status_code == 200
                html_source = response.text
                self._get_info(html_source)
            except AssertionError as e:
                print(f'ERROR: {repr(e)}')
                print(response.status_code)

    def _get_info(self, html_source):
        pages_info = BeautifulSoup(html_source, 'html.parser')

        films_names = pages_info.find_all('h2', class_='zagolovki')
        for name in films_names:
            self.items_genre.append(name.text)
            films_urls_kinogo = name.find('a').get('href')
            self.urls_genre.append(films_urls_kinogo)


