from nltk.tokenize import WordPunctTokenizer
from src.utils.logger_setup import logger_setup
from collections import Counter

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

    @staticmethod
    def token_frequency(tokens, log_file='logs/project_logs.log'):
        """
        Calculates the frequency of each token in the list of tokens.

        Parameters:
        tokens (list): The list of tokens.

        Returns:
        dict: A dictionary where the keys are tokens and the values are frequencies.
        """
        # Set up logger
        logger = logger_setup(log_file)

        # Calculate token frequencies
        token_freq = Counter(tokens)

        # Log the number of unique tokens
        logger.info(f'Calculated frequencies for {len(token_freq)} unique tokens')

        return token_freq