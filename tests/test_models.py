import unittest
from src.website.models.database import SessionLocal, Base

class TestModels(unittest.TestCase):
    def test_hotel_model(self):
        db = SessionLocal()
        hotel = db.query(Hotel).first()
        self.assertIsNotNone(hotel)
        db.close()

if __name__ == '__main__':
    unittest.main()