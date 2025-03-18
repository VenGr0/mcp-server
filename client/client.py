import requests

BASE_URL = 'http://127.0.0.1:5000'

def get_exchange_rate():
    response = requests.get(f'{BASE_URL}/exchange_rate')
    return response.json()

def get_weather(city):
    response = requests.get(f'{BASE_URL}/weather?city={city}')
    return response.json()

def get_news():
    response = requests.get(f'{BASE_URL}/news')
    return response.json()

if __name__ == '__main__':
    print(get_exchange_rate())
    print(get_weather('Moscow'))
    print(get_news())