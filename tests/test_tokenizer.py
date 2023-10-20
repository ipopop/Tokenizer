import unittest
from src.tokenizer.tokenizer import Tokenizer  # Update with your actual import path

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()
        self.text = "Your test text here"

    def test_tokenize(self):
        tokens = self.tokenizer.tokenize(self.text)
        # Add assertions here

    def test_token_frequency(self):
        freq = self.tokenizer.token_frequency(self.text)
        # Add assertions here

    def test_word_cloud(self):
        word_cloud = self.tokenizer.generate_word_cloud(self.text)
        # Add assertions here

    def test_remove_stopwords(self):
        text_without_stopwords = self.tokenizer.remove_stopwords(self.text)
        # Add assertions here

    def test_remove_punctuation_and_numbers(self):
        text_without_punct_and_nums = self.tokenizer.remove_punctuation_and_numbers(self.text)
        # Add assertions here

if __name__ == '__main__':
    unittest.main()