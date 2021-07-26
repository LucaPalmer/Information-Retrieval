# MongoDB password: UmIG9O9HrCUxXETt

import json
import pandas as pd

with open('C:/Users/lucap/PycharmProjects/pythonProject/crawlertest/data.json') as f:
    data = json.load(f)

import elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch()

# Add documents to index

es.indices.refresh('test-index')
es.cat.count('test-index', params={"format": "json"})


def add_doc(doc):
    for i in range(len(doc)):
        es.index(index="test-index", id=i, body=doc[i])


# add_doc(data)
es.indices.refresh('test-index')

"""
# Get documents
res = es.get(index="test-index", id=6)
print(res['_source'])
"""

def title_query():
    print("Enter a title: ")
    query = input()
    title_query_body = {
      "query": {
          "match": {
              "Title": query
          }
      }
    }
    title_res = es.search(index = "test-index", body = title_query_body)
    print("query hits:", title_res["hits"]["hits"])

def author_query():
    print("Enter an author name: ")
    query = input()
    author_query_body = {
      "query": {
          "match": {
              "Non-EEC Authors": query
          }
      }
    }
    title_res = es.search(index = "test-index", body = author_query_body)
    print("query hits:", title_res["hits"]["hits"])

def EEC_query():
    print("Enter an author name: ")
    query = input()
    EEC_query_body = {
      "query": {
          "match": {
              "EEC Authors": query
          }
      }
    }
    title_res = es.search(index = "test-index", body = EEC_query_body)
    print("query hits:", title_res["hits"]["hits"])

def year_query():
    print("Enter a year: ")
    query = input()
    year_query_body = {
      "query": {
          "match": {
              "Year": query
          }
      }
    }
    title_res = es.search(index = "test-index", body = year_query_body)
    print("query hits:", title_res["hits"]["hits"])


def search():
    print("Please select a query type")
    print("Type 'title', 'authors', 'eec', 'year'")
    query_select = input()
    if query_select == 'title':
        title_query()
    if query_select == 'authors':
        author_query()
    if query_select == 'eec':
        EEC_query()
    if query_select == 'year':
        year_query()

search()
"""
#SEE ALL DOCUMENTS IN INDEX:
for doc in title_res['hits']['hits']:
    print (doc['_id'], doc['_source'])
"""
