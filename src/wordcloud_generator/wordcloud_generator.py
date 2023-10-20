from wordcloud import WordCloud

class WordcloudGenerator:
    def generate_wordcloud(self, text: str, max_words: int = 200, colormap: str = 'viridis') -> WordCloud:
        wordcloud = WordCloud(max_words=max_words, colormap=colormap).generate(text)
        return wordcloud