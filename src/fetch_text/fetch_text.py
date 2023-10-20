import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch HTML from {url}: {e}")
        return None
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    return soup.get_text()

def clean_text(text):
    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())

    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # Drop blank lines
    return '\n'.join(chunk for chunk in chunks if chunk)

def fetch_text(url):
    html = fetch_html(url)
    if html is None:
        return None

    text = parse_html(html)
    return clean_text(text)