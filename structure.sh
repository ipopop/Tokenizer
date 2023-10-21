#!/bin/bash

# Create directories
mkdir -p src/utils tests/utils logs

# Mark dir as a Python package
touch src/utils/__init__.py tests/utils/__init__.py logs/__init__.py

# Create files
touch src/utils/logger_setup.py tests/utils/test_logger.py logs/project_logs.log



# Create all the rest of the project
mkdir -p src/{fetch_text,tokenizer,wordcloud_generator,stopwords_remover,punctuation_and_number_remover} tests && touch README.md requirements.txt src/__init__.py src/{fetch_text,tokenizer,wordcloud_generator,stopwords_remover,punctuation_and_number_remover}/__init__.py src/{fetch_text/fetch_text,tokenizer/tokenizer,wordcloud_generator/wordcloud_generator,stopwords_remover/stopwords_remover,punctuation_and_number_remover/punctuation_and_number_remover}.py tests/__init__.py tests/test_{fetch_text,tokenizer,wordcloud_generator,stopwords_remover,punctuation_and_number_remover}.py