import unittest
from src.stopwords_remover.stopwords_remover import StopwordsRemover  # Update with your actual import path

class TestStopwordsRemover(unittest.TestCase):
    def setUp(self):
        self.stopwords_remover = StopwordsRemover()

    def test_remove_stopwords(self):
        text_with_stopwords = "This is a sample sentence, showing off the stop words filtration."
        text_without_stopwords = self.stopwords_remover.remove_stopwords(text_with_stopwords)
        self.assertEqual(text_without_stopwords, "sample sentence, showing stop words filtration.")

if __name__ == '__main__':
    unittest.main()