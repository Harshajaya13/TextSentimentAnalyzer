from utils import read_text_file
from keywords import extract_keywords
from sentiment import analyze_sentiment


def main():

    text = read_text_file("sample.txt")

    keywords = extract_keywords(text, 5)

    sentiment = analyze_sentiment(text)

    print("Sentiment:", sentiment)

    print("\nKeywords:")
    for word, count in keywords:
        print(word, count)


if __name__ == "__main__":
    main()
