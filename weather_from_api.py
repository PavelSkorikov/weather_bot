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

if __name__ == '__main__':
    GetForecastFromAPI()
