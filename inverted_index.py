import numpy as np
import pandas as pd
import spacy

data = pd.read_json(r'C:\Users\lucap\PycharmProjects\pythonProject\crawlertest\data.json')  #
"""
# Figure out how to implement docID

#data.reset_index(inplace = True)
#data = data.rename(columns = {'index': 'ID'})
"""
# Convert columns to string format (Spacy only takes string as input).
def string_conv(x):
    x = str(x)
    x = x.replace("\n", " ")
    x = x.lower()
    x = x.strip()
    return (x)

titles = string_conv(data['Title'])
authors = string_conv(data['Non-EEC Authors'])
eec_authors = string_conv(data['EEC Authors'])

nlp = spacy.load("en_core_web_sm")  # Load trained pipeline for Spacy.

# Create documents from using trained pipeline - Tokenisation already occurs here.
titles_docs = nlp(titles)
authors_docs = nlp(authors)
eec_authors_docs = nlp(eec_authors)

"""
# Tokenizer function for tokenising elements into terms - documents must be input into function.
def tokeniser(doc):
    result = []
    for token in doc:
        result.append(token.text)
    return (result)


titles_docs = tokeniser(titles_docs)
author_docs = tokeniser(authors_docs)
eec_authors_docs = tokeniser(eec_authors_docs)
years_docs = tokeniser(years_docs)
"""


# Stop Word function for removing unnecessary terms - Requires (tokenized) documents.
def remove_stop_words(doc):
    tokens = []
    for token in doc:
        if not token.is_stop:
            tokens.append(token.text)
    return (tokens)

# Remove Stop Words
titles_docs = remove_stop_words(titles_docs)
authors_docs = remove_stop_words(authors_docs)
eec_authors_docs = remove_stop_words(eec_authors_docs)

# Convert back to String Format
titles_docs = string_conv(titles_docs)
authors_docs = string_conv(authors_docs)
eec_authors_docs = string_conv(eec_authors_docs)