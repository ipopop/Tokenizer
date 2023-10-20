from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class StopwordsRemover:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def remove_stopwords(self, text: str) -> str:
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if not w in self.stop_words]
        return ' '.join(filtered_text)