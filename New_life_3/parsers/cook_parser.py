from bs4 import BeautifulSoup
import requests

cook_urls = []
cook_description = []


def cook_dessert():
    url = f'https://www.russianfood.com/recipes/bytype/?fid=45'

    response = requests.get(url=url)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    cooks = pages_info.find_all('div', class_='recipe_l in_seen v2')

    for cook in cooks:
        urls = "https://www.russianfood.com"+cook.find('div', class_='title').find('a').get('href')
        description = cook.find('div', class_='title').find('a').text

        cook_urls.append(urls)
        cook_description.append(description)
    return cook_urls, cook_description


parser_cook = cook_dessert()

all_cooks = list(zip(cook_description, cook_urls))
