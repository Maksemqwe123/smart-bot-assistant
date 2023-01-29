from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser_films_kinogo_life2 import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from buttons import *

import random

genre = []


bot = Bot('5958293925:AAGh2IVIUkvGfygLO-ebFbIzU-r0QfZJnAA')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я бот который подскажет какой фильм можно посмотреть🍿🎬', reply_markup=user_kb)


@dp.callback_query_handler(text='films_buttons')
async def films_buttons(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    parse = Parser(range(1, 10))

    all_info = list(zip(items, urls))
    for i in all_info:
        list_kinogo = f'Название: {i[0].strip()} \nСсылка: {i[1]}'
        spend.append(list_kinogo)

    mess = random.choice(spend)
    await bot.send_message(callback_query.from_user.id, f'{mess}', reply_markup=user_kb)


@dp.callback_query_handler(text='genre_film')
async def genre_film(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Выберите ваш любимый жанр фильма❤️‍🔥🎬🍿🏆', reply_markup=user_genre)


@dp.callback_query_handler(text='cartoons')
async def genre_film(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre = list(zip(items_genre, urls_genre))
    for z in all_info_genre:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)

    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='comedy')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='action')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='military')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='drama')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='horror')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='melodrama')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='adventures')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='family')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='fiction')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='thriller')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()


@dp.callback_query_handler(text='anime')
async def genre_film_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    store_buttons_clicked = callback_query.data

    genre.append(store_buttons_clicked)

    parse_genre = ParserGenre(range(1, 4), genre[0])
    all_info_genre_1 = list(zip(items_genre, urls_genre))
    for z in all_info_genre_1:
        list_genre_kinogo = f'Название: {z[0].strip()} \nСсылка: {z[1]}'
        spend_genre.append(list_genre_kinogo)
    random_films = random.choice(spend_genre)
    random_films_2 = random.choice(spend_genre)
    random_films_3 = random.choice(spend_genre)

    await bot.send_message(callback_query.from_user.id, f'{random_films}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_2}')
    await bot.send_message(callback_query.from_user.id, f'{random_films_3}', reply_markup=user_kb)
    items_genre.clear()
    urls_genre.clear()
    genre.clear()
    spend_genre.clear()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
