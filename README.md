# Calendar Service

Telegram bot for displaying the weather in Yaroslavl for 15 days


## Requirements
Python 3.8+, pip3, virtualenv

## Usage
To run the server, please clone this git repository and open project directory
```
git clone https://github.com/PavelSkorikov/weather_bot.git
cd weather_bot
```
Then execute the following from the root directory:
```
virtualenv -p python3.8 ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
./start.sh
```
You can testing Telegram bot by adress:
```
@WorldweatheronlineBot
```

## Running with Docker
To run the server on a Docker container, 
please define you enviroments configuration in docker-compose.yaml.
Then execute the following from the root directory:
```
# building the image and starting up a containers
sudo docker-compose up --build
```
the server will be run
You can testing Telegram bot by adress:
```
@WorldweatheronlineBot
```
