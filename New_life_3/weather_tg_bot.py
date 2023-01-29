from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from New_life_3.config import BOT_TOKEN
from New_life_3.handler import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':
    from New_life_3.handler import dp

    register_handlers_commands(dp)
    register_handlers_weather_house_street(dp)
    register_handlers_back_game(dp)
    register_handlers_eats_drinks(dp)
    register_handlers_film_book(dp)
    register_handlers_location_new_city(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
