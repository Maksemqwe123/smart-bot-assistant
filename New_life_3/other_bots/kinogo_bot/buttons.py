from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

user_kb = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton('Получить фильм🎬', callback_data='films_buttons'),
    InlineKeyboardButton('Выбрать жанры🎥', callback_data='genre_film')).add(
    InlineKeyboardButton('другие наши боты🤖', url='http://t.me/Weather_4553_bot')
)

user_genre = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton('ужасы', callback_data='horror'),
    InlineKeyboardButton('мультфильмы', callback_data='cartoons'),
    InlineKeyboardButton('комедии', callback_data='comedy')
).add(
    InlineKeyboardButton('боевики', callback_data='action'),
    InlineKeyboardButton('военные', callback_data='military'),
    InlineKeyboardButton('драмы', callback_data='drama')
).add(
    InlineKeyboardButton('мелодрамы', callback_data='melodrama'),
    InlineKeyboardButton('приключение', callback_data='adventures'),
    InlineKeyboardButton('семейные', callback_data='family')
).add(
    InlineKeyboardButton('Фантастика', callback_data='fiction'),
    InlineKeyboardButton('Триллеры', callback_data='thriller'),
    InlineKeyboardButton('Аниме', callback_data='anime')
)
