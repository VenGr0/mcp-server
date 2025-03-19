
MCP (Multi-Functional Command Processor) сервер предоставляет API для получения текущего курса доллара, прогноза погоды в заданном городе и сводки новостей за последнюю неделю.

## Возможности

- **Курс доллара:** Получение текущего курса доллара к рублю.
- **Прогноз погоды:** Получение текущей погоды в указанном городе.
- **Сводка новостей:** Получение новостей за последнюю неделю.

## Установка и запуск

### Предварительные требования

- Python 3.7 или выше
- Установленный `pip`

### Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/VenGr0/mcp-server.git
   cd mcp-server
   ```

2. Создайте виртуальное окружение и активируйте его:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

### Запуск сервера

Запустите сервер:

```bash
python server.py
```

Сервер будет доступен по адресу `http://127.0.0.1:5000`.

### Запуск тестов

Для запуска тестов выполните:

```bash
pytest tests/test_server.py
```

## Использование API

### Получение курса доллара

**Запрос:**
```bash
GET /exchange_rate
```

**Ответ:**
```json
{
  "usd_rate": 75.50
}
```

### Получение прогноза погоды

**Запрос:**
```bash
GET /weather?city=Moscow
```

**Ответ:**
```json
{
  "weather": "clear sky",
  "temperature": 20
}
```

### Получение сводки новостей

**Запрос:**
```bash
GET /news
```

**Ответ:**
```json
{
  "articles": [
    {
      "title": "Новость 1",
      "description": "Описание новости 1",
      "url": "https://example.com/news1"
    },
    {
      "title": "Новость 2",
      "description": "Описание новости 2",
      "url": "https://example.com/news2"
    }
  ]
}
```

## Подключение клиента

Пример клиента на Python:

```python
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
```
