import requests
from New_life_3.config import OPEN_WEATHER_TOKEN

ru = 'ru'


def get_weather(city, OPEN_WEATHER_TOKEN):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang={ru}"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print(f'В городе: {city} \nТемпература воздуха: {cur_weather} C \nОжидается: {weather_description}\n'
              f'Скорость ветра: {wind} м/c')

    except Exception as ex:
        print(ex)
        print("Проверьте название города")


def main():
    city = input('Введите город')
    get_weather(city, OPEN_WEATHER_TOKEN)


if __name__ == '__main__':
    main()
