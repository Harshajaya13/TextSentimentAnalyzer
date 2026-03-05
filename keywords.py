from collections import Counter
from nltk.corpus import stopwords
import string

def extract_keywords(text, top_n=5):
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words("english"))
    clean_words = []

    for word in words:
        word = word.strip(string.punctuation)
        if word and word not in stop_words:
            clean_words.append(word)

    freq = Counter(clean_words)
    return freq.most_common(top_n)

