from src.stopwords_remover.stopwords_remover import StopwordsRemover
import unittest

class TestStopwordsRemover(unittest.TestCase):
    def setUp(self):
        self.remover = StopwordsRemover()

    def test_remove_stopwords(self):
        text = "This is a test"
        expected = "This test"
        actual = self.remover.remove_stopwords(text)
        self.assertEqual(expected, actual)