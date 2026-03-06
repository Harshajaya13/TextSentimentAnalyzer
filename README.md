# Text Sentiment Analyzer

## Overview

Text Sentiment Analyzer is a small Natural Language Processing (NLP) project that analyzes text and determines the sentiment expressed in it.
The program classifies input text as **positive**, **negative**, or **neutral** and extracts important keywords from the text.

This project demonstrates basic NLP concepts such as tokenization, sentiment scoring, and keyword extraction using Python.

---

## Features

* Sentiment classification of input text
* Keyword extraction
* Simple modular architecture
* Example input text for testing

---

## Project Structure

```
TextSentimentAnalyzer
│
├── main.py          # Entry point of the application
├── sentiment.py     # Sentiment analysis logic
├── keywords.py      # Keyword extraction
├── utils.py         # Helper functions
│
├── sample.txt       # Example text input
│
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/Harshajaya13/TextSentimentAnalyzer.git
cd TextSentimentAnalyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

Download required NLTK resources:

```
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
```

---

## Usage

Run the program:

```
python main.py
```

The program reads the sample text and outputs:

* Sentiment classification
* Extracted keywords

---

## Example Output

```
Sentiment: Positive

Keywords:
video
partner
editing
AI
```

---

## Technologies Used

* Python
* NLTK (Natural Language Toolkit)
* Regular Expressions

---

## Purpose of the Project

This project was built to explore fundamental NLP techniques and demonstrate how text data can be processed and analyzed using Python.

---

## Future Improvements

* Use machine learning models for sentiment classification
* Support larger datasets
* Build an API interface
* Integrate with speech-to-text pipelines
