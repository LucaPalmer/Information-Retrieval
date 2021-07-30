# TEXT CLASSIFICATION ATTEMPT

import string
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords


"""
from os import listdir
from os.path import isfile, join

# Read all files from folder
filenames = [
    'data/health.txt',
    'data/science.txt',
    'data/sports.txt'
]

data_path = 'C:/Users/lucap/Downloads/data/'
data_files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
corpus = pd.DataFrame()
print(data_files)

# Create dataframes from text files
dfs = []
for f in data_files:
    with open(data_path + f, 'r', encoding='utf-8') as file:
        data = file.read()

    data = data.split('\n')
    label = f.split('.')[0]

    d = pd.DataFrame()
    d['term'] = data
    d['label'] = [label] * len(data)
    d = d[d.term != '']
    dfs.append(d)
"""

# todo: load data

#  load each file's data
with open(r'C:\Users\lucap\Downloads\data\health.txt', 'r', encoding="utf-8") as file:
     health = file.read()

with open(r'C:\Users\lucap\Downloads\data\science.txt', 'r', encoding="utf-8") as file:
     science = file.read()

with open(r'C:\Users\lucap\Downloads\data\sports (1).txt', 'r', encoding="utf-8") as file:
     sports = file.read()

#    make a df of all data
health_df = list(health.split("\n"))
science_df = list(science.split("\n"))
sports_df = list(sports.split("\n"))

health_df = pd.DataFrame(health_df, columns=['term'])
health_df['classification'] = 'health'

science_df = pd.DataFrame(science_df, columns=['term'])
science_df['classification'] = 'science'

sports_df = pd.DataFrame(sports_df, columns=['term'])
sports_df['classification'] = 'sports'

dfs = list([health_df, science_df, sports_df])


#Create corpus from dataframes
corpus = pd.concat(dfs, axis=0)
corpus = corpus[corpus.term != '']
corpus = corpus.reset_index(drop=True)
corpus.to_csv('corpus.csv')

print(corpus)


#    turn all words into a list()
def remove_punct(a_word: str):
    return a_word.translate(str.maketrans('', '', string.punctuation))

vocab = list(corpus['term'])
vocab = {remove_punct(w) for w in vocab}


# tokenize the text;
#  use tfidf
stop_words = list(stopwords.words("english"))

n_grams = (1, 3)
tfidf = TfidfVectorizer(
    ngram_range=n_grams,
    analyzer='word',
    vocabulary=vocab,
    stop_words=stop_words
)

# todo: load train set; a list of sentences, corpus
# corpus = list(corpus)
from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(corpus, test_size=0.2)

train_set = tfidf.fit_transform(train_set)
test_set = tfidf.fit_transform(test_set)

# todo*: feature scaling


# todo: give data to the model to train
model = MultinomialNB()
model.fit(X=train_set['term'], y=test_set['label'])

preds = model.predict(test_set['term'])

# todo: test said model

