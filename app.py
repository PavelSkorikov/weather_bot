from flask import Flask
from os import getenv
from apscheduler.schedulers.background import BackgroundScheduler
import telebot
import re

from weather_from_api import GetForecastFromAPI, GetForecastFromFile

app = Flask(__name__)

"""scheduled task getting weather data from API """
sched = BackgroundScheduler(daemon=True)
sched.add_job (GetForecastFromAPI, 'interval', hours=1)
sched.start()

bot = telebot.TeleBot(getenv('BOT_KEY'))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    date = re.findall('\d{2}\.\d{2}\.\d{4}', message.text)
    if len(date) > 0:
        answer = GetForecastFromFile(date[0])
        if answer['error']:
            answer_str = answer['error']
        else:
            answer_str = answer['description']+'\n Тмакс= '+answer['maxTemp']+'\n Тмин= '+answer['minTemp'] \
                         + '\n Давление= ' + answer['pressure']+ '\n Влажность= ' + answer['humidity']
        bot.send_photo(message.chat.id, answer['img'])
        bot.send_message(message.from_user.id, answer_str)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для получения прогноза погоды на любой из следующих 15 дней - отправь дату в формате дд.мм.гггг")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)

@app.route('/')
def index():
    return 'Привет - это будущий API'


if __name__ == '__main__':
    app.run()

