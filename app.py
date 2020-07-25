from flask import Flask
from os import getenv, name
import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler

from weather_from_api import GetForecastFromAPI

app = Flask(__name__)

"""scheduled task getting weather data from API """
sched = BackgroundScheduler(daemon=True)
sched.add_job (GetForecastFromAPI, 'interval', hours=1)
sched.start()

def GetForecastFromFile(date):
    """getting weather forecast by date from local weather.tmp"""
    day = date.split('.')[::-1]
    with open('weather.tmp', encoding='utf-8') as f:
        d = json.load(f)
        weather = {}
        for item in d['data']['weather']:
            compare = list(set(day) & set(item['date'].split('-')))
            if len(compare) == 3:
                weather['description'] = item['hourly'][0]['lang_ru'][0]['value']
                weather['maxTemp'] = item['maxtempC']
                weather['minTemp'] = item['mintempC']
                weather['pressure'] = item['hourly'][0]['pressure']
                weather['humidity'] = item['hourly'][0]['humidity']
                weather['img'] = item['hourly'][0]['weatherIconUrl'][0]['value']
        if len(weather) == 0:
            return 'this date is not found'
        else:
            return weather




@app.route('/')
def index():
    return GetForecastFromFile('27.07.2020')




if __name__ == '__main__':
    app.run()

