from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# API ключи (замените на свои)
OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'
NEWSAPI_API_KEY = 'your_newsapi_api_key'

@app.route('/exchange_rate', methods=['GET'])
def get_exchange_rate():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return jsonify({'usd_rate': data['rates']['RUB']})

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric')
    data = response.json()
    return jsonify({'weather': data['weather'][0]['description'], 'temperature': data['main']['temp']})

@app.route('/news', methods=['GET'])
def get_news():
    response = requests.get(f'https://newsapi.org/v2/everything?q=Russia&from=2023-10-01&sortBy=publishedAt&apiKey={NEWSAPI_API_KEY}')
    data = response.json()
    return jsonify({'articles': data['articles']})

if __name__ == '__main__':
    app.run(debug=True)