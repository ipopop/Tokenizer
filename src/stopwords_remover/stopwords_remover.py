from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class StopwordsRemover:
    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if not w in stop_words]
        return ' '.join(filtered_text)