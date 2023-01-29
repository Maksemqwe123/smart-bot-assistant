from weather_tg_bot import *

from New_life_3.config import *

from New_life_3.weatear import ru

from buttons import *

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

import asyncio

import logging

from aiogram.dispatcher import FSMContext

from geopy.geocoders import Nominatim

from parsers.parser_location_address import *

from parsers.parser_pizza import *
from New_life_3.parsers.parser_kinogo import *
from New_life_3.parsers.parser_litres import all_books
from New_life_3.parsers.cook_parser import all_cooks
from New_life_3.parsers.parser_restaurant_pizza import *
from New_life_3.parsers.parser_coffee import *
from New_life_3.parsers.parser_cinema import *

from sqlite import Database

import aioschedule

import requests
import random

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
)

db = Database('new_database')

number = random.randint(1, 20)
count_of_attempts = 1

locations_latitude_and_longitude = []
location_no_duplicates = []
locations_latitude_and_longitude_cinema = []
location_no_duplicates_cinema = []
locations_latitude_and_longitude_restaurant = []
location_no_duplicates_restaurant = []

real_location_coffee = []
real_location_cinema = []
real_location_restaurant = []
location_city_name = []


async def start_message(message: types.Message):
    welcome = message.from_user.full_name
    await message.answer(f'Привет {welcome}, я бот который подскажет как провести день, в связи с погодой🌤',
                         reply_markup=user_kb)
    await message.answer('В каком городе ты хочешь узнать погоду?🌤')
    if message.chat.type == 'private':
        db.create_table()
        if not db.create_profile(message.from_user.id):
            db.edit_profile(message.from_user.id, welcome)
            logging.info('Добавлен новый пользователь в бд')
        else:
            logging.info('Новых данных в бд не добавлено')


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Действие отменено❌', reply_markup=house_or_street)


async def send_all(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == ADMIN_ID:
            text = message.text[9:]
            users_id = db.get_users()
            for row in users_id:
                try:
                    await bot.send_message(row[0], text)

                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


async def today(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        await message.answer(
            f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
            f'Скорость ветра: {wind} м/c', reply_markup=house_or_street)

        if 10 < cur_weather < 5:
            await message.answer('Cегодня на улице довольно нестабильная погода☀️☔️🏊‍♂️, '
                                 'возможны перепады температуры🥶🥵, можно остаться дома👨‍💻 или пойти на улицу🚶‍♂🚶‍♀')

        if 5 > cur_weather > -4:
            await message.answer('cегодня на улице немного холодно❄️, возможно слякоть и гололёд🏊‍♂️⛸,'
                                 'можно остаться дома👨‍💻 или пойти на улицу🚶‍♂🚶‍♀')

        elif -4 > cur_weather > -9:
            await message.answer(
                'сейчас на улице холодно❄️, оденься потеплее🧤, желательно ещё поесть перед выходом🍜🍳')

        elif -9 > cur_weather > -16:
            await message.answer('сейчас на улице довольно холодно🥶, посоветую тебе остаться дома👨‍💻,'
                                 'но если тебе не страшен холод, могу посоветовать куда можно сходить🚶‍♂🚶‍♀')

        elif cur_weather < -16:
            await message.answer('cейчас на улице очень холодно🥶☠️, останься лучше дома👨‍💻')

    except:
        await message.reply("Проверьте название города")


async def leisure(message: types.Message):
    await message.answer(
        'можно посмотреть/почитать фильм/книгу, но перед этим,🎬📚 я бы посоветовал заварить чая/кофе.☕\n'
        'могу подсказать как легко и просто приготовить вкусный десерт,🧁'
        'так же проходит акция при заказе пиццы🍕', reply_markup=help_assistant_house)


class DataFilms(StatesGroup):
    Film_cimema = State()


async def street(message: types.Message):
    await DataFilms.Film_cimema.set()

    await message.answer('В каком городе вы хотите посмотреть развлечения🎬☕🍕', reply_markup=user_leisure)


async def leisure_city(message: types.Message, state: FSMContext):
    leisure_city_people = message.text
    location_city_name.append(leisure_city_people)
    await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                         'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                         'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

    await state.finish()


async def back_weather(message: types.Message):
    await message.answer('Погода на сегодня ожидается...', reply_markup=user_kb)


class DataGame(StatesGroup):
    Offer_game = State()


async def game(message: types.Message):
    global count_of_attempts, number

    if count_of_attempts == 1:
        await message.answer(f'Отгадай число \nя загадал число от 1 до 20, попробуй его угадать😉', reply_markup=menu)
    else:
        await message.answer(f'Введите число🧐')

    await DataGame.Offer_game.set()


async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('секунду⏱', reply_markup=house_or_street)


@dp.callback_query_handler(text='back_call')
async def back_call(callback_query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await bot.send_message(callback_query.from_user.id, 'секунду⏱', reply_markup=house_or_street)


async def back_street(message: types.Message):
    await message.answer('Сейчас подскажу', reply_markup=help_assistant_street)


async def back_house(message: types.Message):
    await message.answer('Сейчас подскажу', reply_markup=help_assistant_house)


async def pizza(message: types.Message):
    for sort_parser_pizza in all_parser_pizza[1:4]:
        await message.answer(sort_parser_pizza[0])


async def kinogo(message: types.Message):
    for sort_kinogo_no_duplicates in kinogo_no_duplicates[1:4]:
        await message.answer(f'Название: {sort_kinogo_no_duplicates[0]} \nCсылка: {sort_kinogo_no_duplicates[-1]}')
    await message.answer('Хочешь посмотреть больше фильмов и выбрать свой любимый жанр❓'
                         '\nУ нас есть бот "I love you kinogo" который поможет вам с '
                         'выбором фильма🍿🎬', reply_markup=bot_films)


async def book(message: types.Message):
    for sort_all_books in all_books[1:4]:
        await message.answer(f'Название:{sort_all_books[0]} \nCcылка: {sort_all_books[-1]}\n')


async def cook(message: types.Message):
    for sort_all_cooks in all_cooks[1:4]:
        await message.answer(f'Название: {sort_all_cooks[0]} \nCcылка: {sort_all_cooks[-1]}\n')


class DataCinema(StatesGroup):
    Loc_cinema = State()


async def cinema(message: types.Message):
    parser_cinema = ParserGenre(location_city_name)
    all_cinema = list(zip(items_genre, urls_genre))
    for sort_all_cinema in all_cinema[1:4]:
        await message.answer(
            f'Название: {sort_all_cinema[0]} \nCcылка: {sort_all_cinema[1]}', reply_markup=types.ReplyKeyboardRemove()
        )
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кинотеатре который находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)

    db.create_table()

    await DataCinema.Loc_cinema.set()


async def location_cinema(message: types.Message, state: FSMContext):
    geolocator_cinema = Nominatim(user_agent="Cinema")
    for sort_loc_address_cinema in loc_address_cinema:
        geolocation_cinema = geolocator_cinema.geocode(sort_loc_address_cinema, timeout=10)
        if geolocation_cinema is None:
            locations_latitude_and_longitude_cinema.append(None)
        else:
            locations_cinema = geolocation_cinema.latitude, geolocation_cinema.longitude

            locations_latitude_and_longitude_cinema.append(locations_cinema)

    geolocation_no_duplicates_cinema = list(set(locations_latitude_and_longitude_cinema))
    loc_geo_cinema = list(filter(None, geolocation_no_duplicates_cinema))

    if message.location is not None:
        geolocation_me_cinema = (message.location.latitude, message.location.longitude)
        for add_location_db in geolocation_me_cinema:
            real_location_cinema.append(add_location_db)

        ab_cinema = loc_geo_cinema[:]
        ab_cinema.append(geolocation_me_cinema)
        ab_cinema.sort()

        db.update_location(latitude=real_location_cinema[0], longitude=real_location_cinema[1], user_id=message.from_user.id)
        logging.info('В бд добавлено новые данные о пользователе')

        ab_index_cinema = ab_cinema.index(geolocation_me_cinema) - 1 if ab_cinema.index(
            geolocation_me_cinema) > 0 else 1
        spend_cinema = (ab_cinema[ab_index_cinema])

        await bot.send_location(message.chat.id, spend_cinema[0], spend_cinema[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Location_cinema')
        location_address = nom.reverse(spend_cinema)
        await message.answer(f'Находится: {location_address}')

        async with state.proxy() as data:
            data["answer1"] = location_address

        await state.finish()


class DataRestaurant(StatesGroup):
    Loc_restaurant = State()


async def restaurant(message: types.Message):
    parser_cinema = ParserRestaurant(location_city_name)
    all_pizza = list(zip(items_restaurant, urls_restaurant, address_restaurant))
    for sort_all_pizza in all_pizza[1:4]:
        await message.answer(
            f'Название: {sort_all_pizza[0]} \nCcылка: {sort_all_pizza[1]}'
            f'\nНаходится: {sort_all_pizza[2]} ', reply_markup=types.ReplyKeyboardRemove())

    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кофейни которая находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)
    db.create_table()

    await DataRestaurant.Loc_restaurant.set()


async def location_restaurant(message: types.Message, state: FSMContext):
    geolocator_restaurant = Nominatim(user_agent="Restaurant")
    for restaurant_city in address_restaurant:
        geolocation_restaurant = geolocator_restaurant.geocode(restaurant_city, timeout=10)
        if geolocation_restaurant is None:
            locations_latitude_and_longitude_restaurant.append(None)
        else:
            locations_restaurant = geolocation_restaurant.latitude, geolocation_restaurant.longitude

            locations_latitude_and_longitude_restaurant.append(locations_restaurant)

    geolocation_no_duplicates_restaurant = list(set(locations_latitude_and_longitude_restaurant))
    loc_geo_restaurant = list(filter(None, geolocation_no_duplicates_restaurant))

    if message.location is not None:
        geolocation_me_restaurant = (message.location.latitude, message.location.longitude)
        for add_location_db in geolocation_me_restaurant:
            real_location_restaurant.append(add_location_db)

        ab_restaurant = loc_geo_restaurant[:]
        ab_restaurant.append(geolocation_me_restaurant)
        ab_restaurant.sort()

        db.update_location(latitude=real_location_restaurant[0], longitude=real_location_restaurant[1], user_id=message.from_user.id)
        logging.info('В бд добавлено новые данные о пользователе')

        ab_index_restaurant = ab_restaurant.index(geolocation_me_restaurant) - 1 if ab_restaurant.index(
            geolocation_me_restaurant) > 0 else 1

        spend_restaurant = (ab_restaurant[ab_index_restaurant])
        await bot.send_location(message.chat.id, spend_restaurant[0], spend_restaurant[1],
                                reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Restaurant')
        location_address_restaurant = nom.reverse(spend_restaurant)
        await message.answer(f'Находится: {location_address_restaurant}')

        async with state.proxy() as data:
            data["answer3"] = location_address_restaurant

        await state.finish()


class DataCoffee(StatesGroup):
    Loc_coffee = State()


async def coffee(message: types.Message):
    parser_cinema = ParserCoffee(location_city_name)
    all_coffee = list(zip(items_coffee, urls_coffee, address_coffee))
    for sort_all_coffee in all_coffee[1:4]:
        await message.answer(
            f'Название: {sort_all_coffee[0]} \nCcылка: {sort_all_coffee[1]} '
            f'\nАдрес: {sort_all_coffee[2]}', reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f'Добавлена новая функция❗ \nМожно узнать о ближайшей кофейни которая находится возле тебя🧭'
                         f' \nФункция работает только на телефоне📱',
                         reply_markup=me_location)
    db.create_table()

    await DataCoffee.Loc_coffee.set()


async def location_coffee(message: types.Message, state: FSMContext):
    geolocator = Nominatim(user_agent="Location_coffee")
    for coffee_city in address_coffee:
        geolocation_coffee = geolocator.geocode(coffee_city, timeout=10)
        if geolocation_coffee is None:
            locations_latitude_and_longitude.append(None)
        else:
            locations = geolocation_coffee.latitude, geolocation_coffee.longitude

            locations_latitude_and_longitude.append(locations)

    geolocation_no_duplicates = list(set(locations_latitude_and_longitude))
    loc_geo = list(filter(None, geolocation_no_duplicates))

    if message.location is not None:
        geolocation_me = (message.location.latitude, message.location.longitude)
        for add_location_db in geolocation_me:
            real_location_coffee.append(add_location_db)

        db.update_location(latitude=real_location_coffee[0], longitude=real_location_coffee[1], user_id=message.from_user.id)
        logging.info('В бд добавлено новые данные о пользователе')

        ab = loc_geo[:]
        ab.append(geolocation_me)
        ab.sort()
        ab_index = ab.index(geolocation_me) - 1 if ab.index(geolocation_me) > 0 else 1
        spend = (ab[ab_index])
        await bot.send_location(message.chat.id, spend[0], spend[1], reply_markup=help_assistant_street)

        nom = Nominatim(user_agent='Location_coffee')
        location_address = nom.reverse(spend)
        await message.answer(f'Находится: {location_address}')

        async with state.proxy() as data:
            data["answer2"] = location_address

        await state.finish()


class Other(StatesGroup):
    Other_city = State()


async def other_city(message: types.Message):
    location_city_name.clear()
    items_restaurant.clear()
    urls_restaurant.clear()
    address_restaurant.clear()
    locations_latitude_and_longitude_restaurant.clear()

    items_coffee.clear()
    urls_coffee.clear()
    address_coffee.clear()
    locations_latitude_and_longitude.clear()

    await Other.Other_city.set()

    await message.answer('В каком городе вы хотите посмотреть развлечения🎬☕🍕', reply_markup=user_leisure)


async def new_city(message: types.Message, state: FSMContext):
    new_city_people = message.text
    location_city_name.append(new_city_people)
    await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                         'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                         'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

    await state.finish()


async def info_game(message: types.Message, state: FSMContext):
    global number, count_of_attempts

    async with state.proxy() as data:
        data["answer2"] = count_of_attempts

    await state.finish()

    try:
        if int(message.text) == number:
            await message.answer(f'Вы угадали!🎉\nКоличество попыток: {count_of_attempts}', reply_markup=house_or_street)
            restart_game = count_of_attempts - 1
            count_of_attempts -= restart_game
            number = random.randint(1, 20)

        elif int(message.text) < number:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число больше')
            count_of_attempts += 1
            await game(message)

        else:
            await message.answer(f'Попробуйте ещё раз🙃 \nЗагаданное число меньше')
            count_of_attempts += 1
            await game(message)
    except ValueError:
        await message.answer(f'Ошибка❗\nДанные должны иметь числовой тип')
        await game(message)


async def send_reminder():
    all_info = db.all_user_db()
    for all_user in all_info:
        id_user = all_user[0]
        full_name = all_user[2]
        await bot.send_message(chat_id=id_user, text=f'Привет {full_name}, хочешь узнать на сегодня погоду?🙃')


async def scheduler():
    aioschedule.every().day.at("9:30").do(send_reminder)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_message, commands='start', state='*')
    dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
    dp.register_message_handler(send_all, commands='sendall', state='*')


def register_handlers_weather_house_street(dp: Dispatcher):
    dp.register_message_handler(today, Text(equals=cities, ignore_case=True))
    dp.register_message_handler(leisure, Text(equals='Что можно поделать дома ?🏠', ignore_case=True))
    dp.register_message_handler(street, Text(equals='Как можно провести время на улице ?🚶‍♂🚶‍♀', ignore_case=True),
                                state=None)
    dp.register_message_handler(leisure_city, state=DataFilms.Film_cimema)


def register_handlers_back_game(dp: Dispatcher):
    dp.register_message_handler(back_weather, Text(equals='Узнать погоду в городе🌤', ignore_case=True))
    dp.register_message_handler(game, Text(equals='Сыграть в игру🔮', ignore_case=True), state=None)
    dp.register_message_handler(info_game, state=DataGame.Offer_game)
    dp.register_message_handler(back, Text(equals='Выйти в главное меню📋', ignore_case=True), state='*')
    dp.register_message_handler(back_street, Text(equals='Как можно провести время на улице ?🚶‍♂🚶‍♀', ignore_case=True))
    dp.register_message_handler(back_house, Text(equals='Что можно поделать дома ?🏠', ignore_case=True))


def register_handlers_eats_drinks(dp: Dispatcher):
    dp.register_message_handler(pizza, Text(equals='Что за акция на пиццу?🍕', ignore_case=True))
    dp.register_message_handler(cook, Text(equals='Какой десерт можно легко приготовить?🧁', ignore_case=True))
    dp.register_message_handler(restaurant, Text(equals='Куда можно сходить поесть ?🍽', ignore_case=True), state=None)
    dp.register_message_handler(coffee, Text(equals='Где и какой кофе можно выпить?☕️', ignore_case=True), state=None)


def register_handlers_film_book(dp: Dispatcher):
    dp.register_message_handler(kinogo, Text(equals='Какой фильм можно посмотреть?🎬', ignore_case=True))
    dp.register_message_handler(book, Text(equals='Какую книгу можно почитать?📚', ignore_case=True))
    dp.register_message_handler(cinema, Text(equals='На какой фильм в кинотеатр можно сходить ?🎬', ignore_case=True),
                                state=None)


def register_handlers_location_new_city(dp: Dispatcher):
    dp.register_message_handler(location_cinema, content_types=["location"], state=DataCinema.Loc_cinema)
    dp.register_message_handler(location_restaurant, content_types=["location"], state=DataRestaurant.Loc_restaurant)
    dp.register_message_handler(location_coffee, content_types=["location"], state=DataCoffee.Loc_coffee)
    dp.register_message_handler(other_city, Text(equals='Выбрать другой город🏙️🌃', ignore_case=True), state=None)
    dp.register_message_handler(new_city, state=Other.Other_city)
