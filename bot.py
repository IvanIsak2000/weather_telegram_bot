import json
import telebot
import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime

bot = telebot.TeleBot("YOUR TELEGRAM BOT API")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Напиши название города (например,москва )или напиши  /help\n Hey! Write the name of the city (for example, moscow) or write /help")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "    \n   Этот бот отображает погоду в определенном городе! Пожалуйста, напишите мне название города (В русском языке можно сочетать прописные и строчные буквы, но не делайте ошибок. Это также правильно: МоСкВа)  \n \nThis bot displays the weather in a certain city! Please write me the name of the city (In russian, you can combine upper and lower case letters, but don't make mistakes. This is also correct: MoSkVa) \n Ссылка/Link: https://github.com/IvanIsak2000/weather_telegram_bot ")


@bot.message_handler(content_types=["text"])
def echo_all(message):

    bot.reply_to(message, "Поиск...(ожидайте) / Scan...(wait)")
    
    time.sleep(2)
    
    city = message.text.lower()
    try:
        if "-" in city:
            cities = city.split("-")  # [санкт][петербург]
            user_city = ""
            for city in cities:

                user_city += city[0].upper() + city[1::].lower()
                user_city += "|"
                user_city = user_city.replace("|", "-")
            user_city_len = len(user_city)
            user_city = user_city[:user_city_len - 1]
        else:
            city = message.text.lower()
            first_city = city[0]
            user_city = str((city.replace(city[0], city[0].upper())))
    except BaseException:
        user_city = "NONE"

    print(user_city)

    date = datetime.today()  # Настройка времени и даты
    now_time = date.strftime('%H:%M:%S')
    day = datetime.now().date()

    with open("_all.json", "r", encoding="utf8") as file:
        file = file.read()
        text = json.loads(file)
        names = []
    for name in text["city"]:
        names += name["name"].split()
    cities = []
    for city in names:
        cities += city.split()

    if user_city in cities:
        print("есть")
        site = ("https://www.google.com/search?q=погода+в+" + str(user_city.split()) + "&hl=ru&sxsrf=ALiCzsaDFVg-mJ46G9JY1k2woiVs07EDkw%3A1671210270761&source=hp&ei=HqWcY4jKLOGGwPAP9cKtgAo&iflsig=AJiK0e8AAAAAY5yzLqFF0IHK5muOVlySe3enRck5K4dR&ved=0ahUKEwiI0aC0z_77AhVhAxAIHXVhC6AQ4dUDCAc&uact=5&oq=погода+в+моске&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEIMBEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6BAgjECc6CwgAEIAEELEDEIMBOgUIABCABDoICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgwIIxAnEJ0CEEYQgAI6DggAEIAEELEDEIMBEMkDUABYpBBgzRFoAHAAeACAAeEBiAGvDJIBBTcuNi4xmAEAoAEB&sclient=gws-wiz")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
        full_page = requests.get(site, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "q8U8x"})
        convert_1 = soup.findAll("span", {"id": "wob_dc"})
        d = ""
        for temperature in convert:
            d += temperature.getText() + " "
        for weah_r in convert_1:
            d += weah_r.getText()
        answer = "Погода в городе / Weather in city: " + \
            str(user_city) + " " + str(d)

    else:
        answer = "Такого города нет! / There is no such city!"

    bot.reply_to(message, answer)
    print(user_city,
          message.from_user.id,
          message.from_user.first_name,
          message.from_user.last_name,
          message.from_user.username,
          "(", now_time, day, ")\n--------------------")
bot.infinity_polling()
