from os import getenv
import json
import requests
import dotenv

dotenv.load_dotenv('.env')

def GetForecastFromAPI():
    """getting 14 days forecast weather from  api.worldweatheronline.com """
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?q=Ярославль&format=json&lang=ru&cc=no&mca=no&tp=24\
    &num_of_days=14&key='+getenv('API_KEY')
    with open('weather.tmp', 'w', encoding='utf-8') as f:
        try:
            json.dump(requests.get(url).json(), f, sort_keys=True, indent=2, ensure_ascii=False)
            print('weather is writed')
        except Exception as e:
            print(e)

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
                weather['maxTemp'] = item['maxtempC']+'C'
                weather['minTemp'] = item['mintempC']+'C'
                pressure = int(item['hourly'][0]['pressure'])*0.075
                weather['pressure'] = str(int(pressure))+'мм.рт.ст.'
                weather['humidity'] = item['hourly'][0]['humidity']+'%'
                weather['img'] = item['hourly'][0]['weatherIconUrl'][0]['value']
                weather['error'] = ''
        if len(weather) == 0:
            weather['error'] = 'Введенная дата выходит за рамки допустимого диапазона'
        return weather

if __name__ == '__main__':
    GetForecastFromAPI()
