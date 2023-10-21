from src.tokenizer.tokenizer import Tokenizer
import unittest

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize(self):
        text = "This is a test"
        expected = ["This", "is", "a", "test"]
        actual = self.tokenizer.tokenize(text)
        self.assertEqual(expected, actual)

    def test_token_frequency(self):
        tokens = ["This", "is", "a", "test", "test"]
        expected = {"This": 1, "is": 1, "a": 1, "test": 2}
        actual = self.tokenizer.token_frequency(tokens)
        self.assertEqual(expected, actual)