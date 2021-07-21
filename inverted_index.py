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

print("Converting to Spacy Document...")

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

print("Removing Punctuation...")

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

print("Removing Whitespace...")

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

print("Removing Stop Words...")

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

print("Lemmatising Tokens...")

titles_doc = lemmatise(titles_doc)
authors_doc = lemmatise(authors_doc)
eec_authors_doc = lemmatise(eec_authors_doc)

titles_doc = punc_remove(titles_doc)
authors_doc = punc_remove(authors_doc)
eec_authors_doc = punc_remove(eec_authors_doc)

# EXPORT TO DICTIONARY, SWAP TERMS AS KEYS AND DOC IDS AS VALUES, CONVERT BACK TO INVERTED INDEX

print("Documents Lemmatised.")

# Creating Hash Table for Terms and Frequency - TRY WITH TITLES ONLY
import hashedindex

titles_doc = str(titles_doc).split(",")
authors_doc = str(authors_doc).split(",")
eec_authors_doc = str(eec_authors_doc).split(",")

doc1 = hashedindex.HashedIndex()
# doc2 = hashedindex.HashedIndex()
# doc3 = hashedindex.HashedIndex()

for term in titles_doc:
    doc1.add_term_occurrence(term, 'doc1')

for term in authors_doc:
    doc1.add_term_occurrence(term, 'doc2')

for term in eec_authors_doc:
    doc1.add_term_occurrence(term, 'doc3')

"""
print("Creating Inverted Index...")

def inverted_index(x):
    for term in x:
        index.add_term_occurrence(term, 'document1')
    return(x)

titles_index = inverted_index(titles_doc)
"""

def test_merge_index_single(self):
    assert hashedindex.merge([self.first_index]) == self.first_index