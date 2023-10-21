import os
import time
from src.fetch_text.fetch_text import FetchText
from src.tokenizer.tokenizer import Tokenizer
from src.punctuation_and_number_remover.punctuation_and_number_remover import PunctuationAndNumberRemover
from src.stopwords_remover.stopwords_remover import StopwordsRemover
from src.wordcloud_generator.wordcloud_generator import WordcloudGenerator
from src.utils.logger_setup import logger_setup

# Initialize the logger
logger = logger_setup('logs/project_logs.log')

def main():
    # Create instances of the classes
    fetch_text = FetchText()
    tokenizer = Tokenizer()
    punctuation_and_number_remover = PunctuationAndNumberRemover()
    stopwords_remover = StopwordsRemover()
    wordcloud_generator = WordcloudGenerator()

    # Sample text
    text = "This is a sample sentence, showing off the stop words filtration and word cloud generation."

    # Fetch text
    start_time = time.time()
    html = fetch_text.fetch_html('http://www.gutenberg.org/files/1342/1342-0.txt')  # replace with your URL
    text = fetch_text.parse_html(html)
    text = fetch_text.clean_text(text)
    end_time = time.time()
    logger.info(f"1. Fetch text...✅ ({(end_time - start_time) * 1000} ms)")

    # Tokenize the text
    start_time = time.time()
    tokens = tokenizer.tokenize(text)
    end_time = time.time()
    logger.info(f"2. Tokenize the text...✅ ({(end_time - start_time) * 1000} ms)")

    # Remove punctuation and numbers
    start_time = time.time()
    text_without_punctuation_and_numbers = punctuation_and_number_remover.remove_punctuation_and_numbers(text)
    end_time = time.time()
    logger.info(f"3. Remove punctuation and numbers...✅ ({(end_time - start_time) * 1000} ms)")

    # Remove stopwords
    start_time = time.time()
    text_without_stopwords = stopwords_remover.remove_stopwords(text_without_punctuation_and_numbers)
    end_time = time.time()
    logger.info(f"4. Remove 'stopwords' from the original text...✅ ({(end_time - start_time) * 1000} ms)")

    # Generate wordcloud
    start_time = time.time()
    wordcloud = wordcloud_generator.generate_wordcloud(text_without_stopwords)
    end_time = time.time()
    logger.info(f"5. Experiment with the 'WordCloud()' parameters to generate different word clouds from the original text...✅ ({(end_time - start_time) * 1000} ms)")

    # Create a directory for the wordcloud images if it doesn't exist
    os.makedirs("wordclouds", exist_ok=True)

    # Get the current time to use in the filename
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Save the wordcloud image in the wordclouds directory with a unique filename
    wordcloud.to_file(f"wordclouds/wordcloud-{timestamp}.png")

    # Get a list of all wordcloud images, sorted by creation time
    wordcloud_images = sorted(os.listdir("wordclouds"), key=lambda x: os.path.getctime(os.path.join("wordclouds", x)))

    # If there are more than 100 images, delete the oldest ones
    while len(wordcloud_images) > 100:
        os.remove(os.path.join("wordclouds", wordcloud_images.pop(0)))

    logger.info(f"Word cloud generated and saved as wordclouds/wordcloud-{timestamp}.png")

if __name__ == "__main__":
    main()