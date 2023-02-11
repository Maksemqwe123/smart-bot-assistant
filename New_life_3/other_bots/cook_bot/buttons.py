# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

user_kb = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton('Указать продукты🍯🌰🥛', callback_data='dessert_product')
).add(
    InlineKeyboardButton('Выбрать рецепт десерта🍰', callback_data='choose_dessert')
).add(
    InlineKeyboardButton('другие наши боты🤖', url='http://t.me/Weather_4553_bot')
)

user_dessert = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton('Пироги', callback_data='Пироги'),
    InlineKeyboardButton('Торты', callback_data='Торты'),
    InlineKeyboardButton('Фруктовые салаты', callback_data='Фруктовые салаты')
).add(
    InlineKeyboardButton('Печенье', callback_data='Печенье'),
    InlineKeyboardButton('Пирожные', callback_data='Пирожные'),
    InlineKeyboardButton('Суфле', callback_data='Суфле')
).row(
    InlineKeyboardButton('Чизкейк', callback_data='Чизкейк'),
    InlineKeyboardButton('Эклер', callback_data='Эклер'),
    InlineKeyboardButton('Кексы', callback_data='Кексы'),
    InlineKeyboardButton('Муссы', callback_data='Муссы')
).row(
    InlineKeyboardButton('Фонтан', callback_data='Фонтан'),
    InlineKeyboardButton('Конфеты', callback_data='Конфеты'),
    InlineKeyboardButton('Мороженое', callback_data='Мороженое')
)
