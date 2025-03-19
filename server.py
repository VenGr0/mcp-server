from flask import Flask, jsonify, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# API ключи (замените на свои)
OPENWEATHERMAP_API_KEY = '538cf094d58ab41a51c9fc41983dd163'  # Ключ для OpenWeatherMap
GUARDIAN_API_KEY = '713774f2-c27c-4553-adda-ec28dd30236f'  # Ключ для The Guardian

@app.route('/exchange_rate', methods=['GET'])
def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return jsonify({'usd_rate': data['rates']['RUB']})

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={
            'q': city,
            'appid': OPENWEATHERMAP_API_KEY,
            'units': 'metric'
        }
    )
    data = response.json()
    
    if response.status_code == 200:
        return jsonify({
            'weather': data['weather'][0]['description'],
            'temperature': data['main']['temp']
        })
    else:
        return jsonify({'error': 'Failed to fetch weather data', 'response': data}), 500

@app.route('/news', methods=['GET'])
def get_news():
    try:
        # Вычисляем дату неделю назад
        one_week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        
        # Запрос к The Guardian API
        response = requests.get(
            'https://content.guardianapis.com/search',
            params={
                'q': 'Russia',  # Ключевые слова для поиска
                'from-date': one_week_ago,  # Новости за последнюю неделю
                'show-fields': 'headline,trailText,webUrl',  # Поля, которые хотим получить
                'api-key': GUARDIAN_API_KEY  # Ваш API-ключ
            }
        )
        data = response.json()
        
        # Отладочная информация
        print("Response from The Guardian API:", data)  # Вывод ответа в консоль
        
        if response.status_code == 200 and 'response' in data:
            articles = data['response']['results']
            return jsonify({'articles': articles})
        else:
            return jsonify({'error': 'Failed to fetch news', 'response': data}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)