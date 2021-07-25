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


title_query_body = {
  "query": {
      "match": {
          "Type": "journal"
      }
  }
}

title_res = es.search(index = "test-index", body = title_query_body)

print("query hits:", title_res["hits"]["hits"])

#SEE ALL DOCUMENTS IN INDEX:
for doc in title_res['hits']['hits']:
    print (doc['_id'], doc['_source'])

