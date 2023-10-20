import unittest
from src.fetch_text.fetch_text import fetch_text

class TestFetchText(unittest.TestCase):
    def test_fetch_text_from_wikipedia(self):
        url = "https://en.wikipedia.org/wiki/Natural_language_processing"
        text = fetch_text(url)
        self.assertIsNotNone(text)
        self.assertTrue(isinstance(text, str))

    def test_fetch_text_from_gutenberg(self):
        url = "http://www.gutenberg.org/files/1342/1342-0.txt"  # Example URL, replace with actual Gutenberg text URL
        text = fetch_text(url)
        self.assertIsNotNone(text)
        self.assertTrue(isinstance(text, str))

    # Add more tests as needed for other sources

if __name__ == '__main__':
    unittest.main()