from nltk.tokenize import WordPunctTokenizer
from src.utils.logger_setup import logger_setup

class Tokenizer:
    """A class used to tokenize text and perform related tasks."""

    @staticmethod
    def tokenize(text, log_file='logs/project_logs.log'):
        """
        Tokenizes the input text.

        Parameters:
        text (str): The text to tokenize.

        Returns:
        list: A list of tokens.
        """
        # Set up logger
        logger = logger_setup(log_file)

        # Tokenize the text
        tokenizer = WordPunctTokenizer()
        tokens = tokenizer.tokenize(text)

        # Log the number of tokens generated
        logger.info(f'Generated {len(tokens)} tokens')

        return tokens