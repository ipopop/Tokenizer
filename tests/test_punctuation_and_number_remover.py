from src.punctuation_and_number_remover.punctuation_and_number_remover import PunctuationAndNumberRemover
import unittest

class TestPunctuationAndNumberRemover(unittest.TestCase):
    def setUp(self):
        self.remover = PunctuationAndNumberRemover()

    def test_remove_punctuation_and_numbers(self):
        text = "Hello, world! 123"
        expected = "Hello world "
        actual = self.remover.remove_punctuation_and_numbers(text)
        self.assertEqual(expected, actual)