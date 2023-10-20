import string

class PunctuationAndNumberRemover:
    """
    A class used to remove punctuation and numbers from a text.
    """

    def __init__(self):
        self.trans_table = str.maketrans('', '', string.punctuation + string.digits)

    def remove_punctuation_and_numbers(self, text):
        """
        Removes all punctuation and numbers from the input text.

        Parameters:
        text (str): The text to remove punctuation and numbers from.

        Returns:
        str: The text with punctuation and numbers removed.
        """
        return text.translate(self.trans_table)