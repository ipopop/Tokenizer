from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import logging

class StopwordsRemover:
    def __init__(self, logger=None):
        self.stop_words = set(stopwords.words('english'))
        self.logger = logger or logging.getLogger(__name__)

    def remove_stopwords(self, text: str) -> str:
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if not w in self.stop_words]
        self.logger.info(f"Removed stopwords from text. Original length: {len(word_tokens)}, Filtered length: {len(filtered_text)}")
        return ' '.join(filtered_text)