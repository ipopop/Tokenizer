# Text Processing and Wordcloud Generation 📚🖼️

This is a Python project that processes text and generates a word cloud (generate png in 'wordclouds/' dir), an example to use tokenization and Natural Language Processing (NLP) techniques. The project follows the principles of clean architecture and uses a three-step Test-Driven Development (TDD) approach.

The detail of process :

1. Find a webpage, a text, or any other NLP dataset.

2. Tokenize the text using NLTK 'WordPunctTokenizer'.

3. Explore the list of 'tokens' and their frequency.

4. Experiment with the 'WordCloud()' parameters to generate different word clouds from the original text:

    - collocations = False

    - normalize_plurals = True or False

    - include_numbers = True or False

    - min_word_length

    - stopwords

5. Remove 'stopwords' from the original text.

6. Use 'string.punctuation' and 'string.digits' to remove punctuation and numbers.

## Table of Contents 📝
  - [Installation 📦](#installation-)
  - [Clean Architecture 🏛️](#clean-architecture-️)
  - [Test-Driven Development (TDD) 🧪](#test-driven-development-tdd-)
  - [Execution 🏃‍♀️](#execution-️)
    - [Running Tests](#running-tests)
    - [Running the Application](#running-the-application)
  - [Contributing 🤝](#contributing-)
  - [License 📄](#license-)

## Installation 📦

To install the necessary dependencies, run the following command:

```bash
pip3 install -r requirements.txt
```

## Clean Architecture 🏛️

The project is divided into two main parts: the StopwordsRemover and the WordcloudGenerator.

The StopwordsRemover is responsible for removing common words (like "the", "is", etc.) from the text.
The WordcloudGenerator takes the processed text and generates a word cloud.

## Test-Driven Development (TDD) 🧪

The project uses a three-step TDD approach:

   - Write a failing test. 🚫
   - Write the code to make the test pass. ✅
   - Refactor the code to improve its design and readability. 🔄

The tests are written using the unittest module in Python.

## Execution 🏃‍♀️

### Running Tests

To run the tests, navigate to the directory containing the test files and run the following command:

```bash
python3 -m unittest tests.test_stopwords_remover
python3 -m unittest tests.test_wordcloud_generator
```
and so on...

### Running the Application

To run the application, navigate to the directory containing the main.py file and run the following command:

```bash
python3 main.py
```

This script create word cloud images in the 'wordclouds' directory (100 max).

## Contributing 🤝

If you would like to contribute to the project, please follow the TDD approach and create a pull request with your changes.

## License 📄

This project is licensed under the MIT License.
