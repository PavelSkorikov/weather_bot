from os import getenv
from config import API_KEY
import json
import requests
import dotenv

dotenv.load_dotenv('.env')

import log_config
logger = log_config.logger
log_error = log_config.log_error

@log_error(logger)
def GetForecastFromAPI():
    """getting 14 days forecast weather from  api.worldweatheronline.com """
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?q=Ярославль&format=json&lang=ru&cc=no&mca=no&tp=24\
    &num_of_days=14&key='+API_KEY
    try:
        with open('weather.tmp', 'w', encoding='utf-8') as f:
            try:
                json.dump(requests.get(url).json(), f, sort_keys=True, indent=2, ensure_ascii=False)
                logger.info('weather is getting from api.worldweatheronline.com')
            except Exception as e:
                logger.error(f'error getting from api.worldweatheronline.com {e}')
        logger.info('data is write to file weather.tmp')
    except Exception as e:
        logger.error(f'error write to file weather.tmp {e}')

@log_error(logger)
def GetForecastFromFile(date):
    """getting weather forecast by date from local weather.tmp"""
    day = date.split('.')[::-1]
    try:
        with open('weather.tmp', encoding='utf-8') as f:
            d = json.load(f)
            weather = {}
            for item in d['data']['weather']:
                compare = list(set(day) & set(item['date'].split('-')))
                if len(compare) == 3:
                    weather['description'] = item['hourly'][0]['lang_ru'][0]['value']
                    weather['maxTemp'] = item['maxtempC']+'C'
                    weather['minTemp'] = item['mintempC']+'C'
                    pressure = int(item['hourly'][0]['pressure'])*0.075
                    weather['pressure'] = str(int(pressure))+'мм.рт.ст.'
                    weather['humidity'] = item['hourly'][0]['humidity']+'%'
                    weather['img'] = item['hourly'][0]['weatherIconUrl'][0]['value']
                    weather['error'] = ''
            if len(weather) == 0:
                weather['error'] = 'Введенная дата выходит за рамки допустимого диапазона'
        logger.info('data is read from file weather.tmp')
    except Exception as e:
        logger.error(f'error read from file weather.tmp {e}')
    return weather

if __name__ == '__main__':
    GetForecastFromAPI()
