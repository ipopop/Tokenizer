import unittest
from src.wordcloud_generator.wordcloud_generator import WordcloudGenerator

class TestWordcloudGenerator(unittest.TestCase):
    def setUp(self):
        self.wordcloud_generator = WordcloudGenerator()

    def test_generate_wordcloud(self):
        text = "This is a sample sentence, showing off the word cloud generation."
        wordcloud_image = self.wordcloud_generator.generate_wordcloud(text)
        self.assertIsNotNone(wordcloud_image)

if __name__ == '__main__':
    unittest.main()