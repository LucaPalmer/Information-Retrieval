import json
from elasticsearch import Elasticsearch


# Command Line Interface
import fire


with open('C:/Users/lucap/PycharmProjects/pythonProject/crawlertest/data.json') as f:
    data = json.load(f)
es = Elasticsearch()


# Add documents to index

es.indices.refresh('test-index')
es.cat.count('test-index', params={"format": "json"})

def add_doc(doc):
    for i in range(len(doc)):
        es.index(index="test-index", id=i, body=doc[i])
        es.indices.refresh('test-index')

def title():
    print("Enter a title: ")
    query = input()
    title_body = {
      "query": {
          "match": {
              "Title": query
          }
      }
    }
    title_res = es.search(index = "test-index", body = title_body)
    print("query hits:", title_res["hits"]["hits"])

def author():
    print("Enter an author name: ")
    query = input()
    author_body = {
        "query": {
            "match": {
                "Non-EEC Authors": query,
            }
        }
    }
    EEC_author_body = {
        "query": {
            "match": {
                "EEC Authors": query
            }
        }
    }
    author_res = es.search(index="test-index", body=author_body)
    EEC_author_res = es.search(index="test-index", body=EEC_author_body)
    if author_res != "[]":
        print("Non-EEC Authors: ", author_res["hits"]["hits"], "\n")
    else:
        print ("No results found!")
    if EEC_author_res != "[]":
        print("EEC Authors: ", EEC_author_res["hits"]["hits"])
    else:
        print ("No results found!")




def year():
    print("Enter a year: ")
    query = input()
    year_body = {
      "query": {
          "match": {
              "Year": query
          }
      }
    }
    author_res = es.search(index = "test-index", body = year_body)
    print("query hits:", author_res["hits"]["hits"])



if __name__ == '__main__':
    fire.Fire({'title': title,
             'author': author,
             'year': year})
