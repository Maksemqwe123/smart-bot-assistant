# -*- coding: utf-8 -*-
import re
import time

from bs4 import BeautifulSoup
import requests

import undetected_chromedriver

from selenium.webdriver.common.by import By
from undetected_chromedriver.options import ChromeOptions

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72',
}

urls = []
name_desserts = []
dessert_random = []

list_product = []
urls_selenium = []
name_desserts_selenium = []

name_urls = {
    'Пироги': '%CF%E8%F0%EE%E3%E8', 'Торты': '%D2%EE%F0%F2%FB', 'Фруктовые салаты': '%F1%E0%EB%E0%F2%FB',
    'Печенье': '%EF%E5%F7%E5%ED%FC%E5', 'Пирожные': '%EF%E8%F0%EE%E6%ED%FB%E5', 'Суфле': '%F1%F3%F4%EB%E5+',
    'Чизкейк': '%F7%E8%E7%EA%E5%E9%EA+', 'Эклер': '%FD%EA%EB%E5%F0%FB', 'Кексы': '%EA%E5%EA%F1%FB',
    'Муссы': '%EC%F3%F1%F1%FB', 'Фонтан': '%F4%EE%ED%E4%E0%ED', 'Конфеты': '%EA%EE%ED%F4%E5%F2%FB',
    'Мороженое': '%EC%EE%F0%EE%E6%E5%ED%EE%E5'
}


class Parser:
    def __init__(self, pages: range, name: str):
        self.pages = pages
        self.urls = urls
        self.name_desserts = name_desserts
        self.name = name

        self._get_html()

    def _get_html(self):
        for page in self.pages:
            if page == 1:
                url = f'https://www.russianfood.com/search/simple/index.php?ssgrtype=bytype&sskw_title={self.name}&tag_tree%5B1%5D%5B%5D=45&'
            else:
                url = f'https://www.russianfood.com/search/simple/index.php?ssgrtype=bytype&sskw_title={self.name}&tag_tree%5B1%5D%5B%5D=45&page={page}'

            response = requests.get(url=url, headers=headers)

            try:
                assert response.status_code == 200
                html_source = response.text
                self._get_info(html_source)
            except AssertionError as ex:
                print(f'ERROR {repr(ex)}')
                print(response.status_code)

    def _get_info(self, html_source):
        pages_info = BeautifulSoup(html_source, 'html.parser')

        cooks = pages_info.find_all('div', class_='recipe_l in_seen v2')

        for desserts in cooks:
            desserts_urls = desserts.find('div', class_='title').find('a').get('href')

            dessert_name = desserts.find('div', class_='title').find('a').text

            urls_list = ("https://www.russianfood.com" + desserts_urls)

            self.urls.append(urls_list)
            self.name_desserts.append(dessert_name)


class ParserSelenium:
    def __init__(self, name_product: str):
        self.list_product = list_product
        self.urls_selenium = urls_selenium
        self.name_desserts_selenium = name_desserts_selenium
        self.name_product = name_product

        self._get_html()

    def _get_html(self):
        ChromeOptions()
        driver = undetected_chromedriver.Chrome()
        driver.get(f'https://www.russianfood.com/search/simple/index.php?ssgrtype=bytype&sskw_title=&tag_tree%5B1%5D%5B%5D=45&tag_tree%5B2%5D%5B%5D=0&sskw_iplus=&sskw_iminus=&submit=#beforesearchform')

        self._get_info(driver)

    def _get_info(self, driver):

        write_product = driver.find_element(By.NAME, 'sskw_iplus')
        write_product.click()
        write_product.send_keys(self.name_product)
        click_find_desserts = driver.find_element(By.NAME, 'submit')
        click_find_desserts.click()

        driver.get(driver.current_url)
        html_source_selenium = driver.page_source
        pages_info_selenium = BeautifulSoup(html_source_selenium, 'html.parser')

        desserts_name_urls_selenium = pages_info_selenium.find_all('div', class_='title')
        for name in desserts_name_urls_selenium:
            self.name_desserts_selenium.append(name.text)

        cooks_selenium = pages_info_selenium.find_all('div', class_='recipe_l in_seen v2')

        for desserts in cooks_selenium:
            desserts_urls_selenium = desserts.find('div', class_='title').find('a').get('href')
            urls_list = ("https://www.russianfood.com" + desserts_urls_selenium)
            self.urls_selenium.append(urls_list)

        driver.close()
        driver.quit()
