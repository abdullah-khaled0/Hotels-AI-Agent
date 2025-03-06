import unittest
from src.website.app import app

class TestRoutes(unittest.TestCase):
    def test_home_route(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()