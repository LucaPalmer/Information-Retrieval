# MongoDB password: UmIG9O9HrCUxXETt

import json
import pandas as pd
import pymongo # mongodb+srv://Luca:<password>@covcluster.mzkx4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Luca:UmIG9O9HrCUxXETt@covcluster.mzkx4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["coventry"]
collection = db["documents"]

with open('C:/Users/lucap/PycharmProjects/pythonProject/crawlertest/data.json') as f:
  data = json.load(f)


data = json.load(r'C:\Users\lucap\PycharmProjects\pythonProject\crawlertest\data.json')
data = data.applymap(lambda s: s.lower() if type(s) == str else s)
# data['Title'] = data['Title'].apply(word_tokenize)


collection.insert_many(data)






