import requests
from bs4 import BeautifulSoup
from src.utils.logger_setup import logger_setup

# Initialize the logger
logger = logger_setup('logs/project_logs.log')

class FetchText:
    @staticmethod
    def fetch_html(url):
        logger.info(f"Fetching HTML from {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch HTML from {url}: {e}")
            return None
        logger.info("Successfully fetched HTML")
        return response.text

    @staticmethod
    def parse_html(html):
        logger.info("Parsing HTML")
        soup = BeautifulSoup(html, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        logger.info("Successfully parsed HTML")
        return soup.get_text()

    @staticmethod
    def clean_text(text):
        logger.info("Cleaning text")
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())

        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        # Drop blank lines
        cleaned_text = '\n'.join(chunk for chunk in chunks if chunk)
        logger.info("Successfully cleaned text")
        return cleaned_text

    @staticmethod
    def fetch_text(url):
        html = FetchText.fetch_html(url)
        if html is None:
            return None

        text = FetchText.parse_html(html)
        return FetchText.clean_text(text)