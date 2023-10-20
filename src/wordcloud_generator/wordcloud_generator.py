from wordcloud import WordCloud

class WordcloudGenerator:
    def generate_wordcloud(self, text):
        wordcloud = WordCloud().generate(text)
        return wordcloud