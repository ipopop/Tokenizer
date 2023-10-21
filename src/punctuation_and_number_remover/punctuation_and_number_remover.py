import string
import logging

class PunctuationAndNumberRemover:
    def __init__(self, logger=None):
        self.trans_table = str.maketrans('', '', string.punctuation + string.digits)
        self.logger = logger or logging.getLogger(__name__)

    def remove_punctuation_and_numbers(self, text):
        cleaned_text = text.translate(self.trans_table)
        self.logger.info(f"Removed punctuation and numbers from text. Original length: {len(text)}, Cleaned length: {len(cleaned_text)}")
        return cleaned_text