import numpy as np
import pandas as pd
import spacy

data = pd.read_csv(r'C:\Users\lucap\PycharmProjects\pythonProject\crawlertest\data.csv')
nlp = spacy.load("en_core_web_sm")  # Load trained pipeline for Spacy.

# Convert columns to string (Spacy only takes string as input), then to document (sequence of tokens) using Spacy
# pipeline.
def doc_conv(x):
    x = str(x).lower()
    x = x.replace("\n", "")
    x = x.lower()
    x = nlp(x)
    return (x)

titles_doc = doc_conv(data['Title'])
authors_doc = doc_conv(data['Non-EEC Authors'])
eec_authors_doc = doc_conv(data['EEC Authors'])

# Remove punctuation (Convert to function)
def punc_remove(doc):
    tokens = []
    for token in doc:
        if not token.is_punct:
            tokens.append(token)
    tokens = str(tokens)
    tokens = nlp(tokens)
    return (tokens)

titles_doc = punc_remove(titles_doc)
authors_doc = punc_remove(authors_doc)
eec_authors_doc = punc_remove(eec_authors_doc)

# Remove whitespace (Convert to function)
def remove_whitespace(doc):
    tokens = []
    for token in doc:
        if not token.is_space:
            tokens.append(token)
    tokens = str(tokens)
    tokens = nlp(tokens)
    return (tokens)

titles_doc = remove_whitespace(titles_doc)
authors_doc = remove_whitespace(authors_doc)
eec_authors_doc = remove_whitespace(eec_authors_doc)

# Stop Word function for removing unnecessary terms - Requires (tokenized) documents.
def remove_stop_words(doc):
    tokens = []
    for token in doc:
        if not token.is_stop:
            tokens.append(token.text)
    tokens = str(tokens)
    tokens = nlp(tokens)
    return (tokens)


# Remove Stop Words
titles_doc = remove_stop_words(titles_doc)
authors_doc = remove_stop_words(authors_doc)
eec_authors_doc = remove_stop_words(eec_authors_doc)

# Lemmatise function
def lemmatise(doc):
    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_)
    lemmas = str(lemmas)
    lemmas = nlp(lemmas)
    return (lemmas)


titles_doc = lemmatise(titles_doc)
authors_doc = lemmatise(authors_doc)
eec_authors_doc = lemmatise(eec_authors_doc)

titles_doc = punc_remove(titles_doc)
authors_doc = punc_remove(authors_doc)
eec_authors_doc = punc_remove(eec_authors_doc)
"""
# Remove punctuation (Convert to function)
lem_titles_tokens = [token for token in lem_titles_tokens if not token.is_punct]
lem_authors_tokens= [token for token in lem_authors_tokens if not token.is_punct]
lem_eec_authors_tokens = [token for token in lem_eec_authors_tokens if not token.is_punct]
"""
"""
def inverted_index(text):
    inverted = {}
    for
"""