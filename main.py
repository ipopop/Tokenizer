import os
import time
from src.stopwords_remover.stopwords_remover import StopwordsRemover
from src.wordcloud_generator.wordcloud_generator import WordcloudGenerator

def main():
    # Create instances of the classes
    stopwords_remover = StopwordsRemover()
    wordcloud_generator = WordcloudGenerator()

    # Sample text
    text = "This is a sample sentence, showing off the stop words filtration and word cloud generation."

    # Remove stopwords
    text_without_stopwords = stopwords_remover.remove_stopwords(text)

    # Generate wordcloud
    wordcloud = wordcloud_generator.generate_wordcloud(text_without_stopwords)

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

    print(f"Word cloud generated and saved as wordclouds/wordcloud-{timestamp}.png")

if __name__ == "__main__":
    main()