import unittest
from pathlib import Path
from src.analyzer import ProjectAnalyzer

class TestProjectAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ProjectAnalyzer()
    
    def test_detect_languages(self):
        current_dir = Path('.')
        if current_dir.exists():
            languages = self.analyzer._detect_languages(current_dir)
            self.assertIsInstance(languages, list)
    
    def test_count_files(self):
        current_dir = Path('.')
        if current_dir.exists():
            count = self.analyzer._count_files(current_dir)
            self.assertGreater(count, 0)

if __name__ == '__main__':
    unittest.main()
