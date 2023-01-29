from bs4 import BeautifulSoup
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72',
}

items_genre = []
urls_genre = []
spend_genre = []


class ParserGenre:
    def __init__(self, name: list):
        self.name = name
        self.items_genre = items_genre
        self.urls_genre = urls_genre

        self._get_html()

    def _get_html(self):
        url = f'https://bycard.by/afisha/{self.name[0]}/kino?view=top'

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

        films_urls = pages_info.find_all('a', class_='capsule')
        for name in films_urls:
            self.urls_genre.append(f"https://bycard.by{name.get('href')}")

        films_names = pages_info.find_all('p', class_='capsule__title')
        for name in films_names:
            self.items_genre.append(name.text)
