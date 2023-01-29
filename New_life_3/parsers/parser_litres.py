from bs4 import BeautifulSoup
import requests

list_urls = []
litres_description = []


def litres():
    url = f'https://litnet.com/ru/top/fentezi'

    response = requests.get(url=url)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    books = pages_info.find_all('div', class_='row book-item')

    for book in books:
        urls = "https://litnet.com"+book.find('h4', class_='book-title').find('a').get('href')
        description = book.find('h4', class_='book-title').find('a').text

        list_urls.append(urls)
        litres_description.append(description)
    return list_urls, litres_description


book_litres = litres()

all_books = list(zip(litres_description, list_urls))
