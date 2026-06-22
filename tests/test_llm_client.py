import unittest
from src.llm_client import OllamaClient

class TestOllamaClient(unittest.TestCase):
    def setUp(self):
        self.client = OllamaClient()
    
    def test_client_init(self):
        self.assertIsNotNone(self.client.host)
        self.assertIsNotNone(self.client.model)

if __name__ == '__main__':
    unittest.main()
