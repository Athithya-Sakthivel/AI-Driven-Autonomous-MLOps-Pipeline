import unittest
from src.data.ingest_data import fetch_newsapi_data

class TestDataIngestion(unittest.TestCase):
    def test_newsapi(self):
        data = fetch_newsapi_data("AI", 5)
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 0)  # Can be empty but must be a list

if __name__ == "__main__":
    unittest.main()