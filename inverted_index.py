import numpy as np
import pandas as pd
import spacy

data = pd.read_json(r'C:\Users\lucap\PycharmProjects\pythonProject\crawlertest\data.json')  #
"""
# Figure out how to implement docID

#data.reset_index(inplace = True)
#data = data.rename(columns = {'index': 'ID'})
"""

titles = data['Title'].to_string()  # Convert column to string format (Spacy only takes string as input)

"""
authors = data['Non-EEC Authors'].astype(str)
eec_authors = data['EEC Authors'].astype(str)
years = data['Year'].astype(str)
"""

nlp = spacy.load("en_core_web_sm")  # Load trained pipeline for Spacy
titles_doc = nlp(titles)  # Create documents from using trained pipeline


# Tokenizer function - documents must be input into function
def tokeniser(doc):
    result = []
    for token in doc:
        result.append(token.text)
    return(result)

titles_docs = tokeniser(titles_doc)
