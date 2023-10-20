import unittest
from src.punctuation_and_number_remover.punctuation_and_number_remover import PunctuationAndNumberRemover  # Update with your actual import path

class TestPunctuationAndNumberRemover(unittest.TestCase):
    def setUp(self):
        self.punctuation_and_number_remover = PunctuationAndNumberRemover()

    def test_remove_punctuation_and_numbers(self):
        text_with_punct_and_nums = "Hello, world! 123"
        text_without_punct_and_nums = self.punctuation_and_number_remover.remove_punctuation_and_numbers(text_with_punct_and_nums)
        self.assertEqual(text_without_punct_and_nums, "Hello world ")

if __name__ == '__main__':
    unittest.main()