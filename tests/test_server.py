import unittest
from server import app

class ServerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_exchange_rate(self):
        response = self.app.get('/exchange_rate')
        self.assertEqual(response.status_code, 200)

    def test_weather(self):
        response = self.app.get('/weather?city=Moscow')
        self.assertEqual(response.status_code, 200)

    def test_news(self):
        response = self.app.get('/news')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()