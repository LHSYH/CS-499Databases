#!/usr/bin/python
import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def read_document(low, high):
    try:
        findDocument = {"50-Day Simple Moving Average":{"$gt":low,"$lt":high}}
        count=collection.find(findDocument).count()
        print(count)
    except Exception as ve:
        return False
    else:
        return True
      
def main():
    read_document(1,2)

main()
