from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://khalfan45:{password}@khalfan1.rd2nmx9.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

dbs = client.list_database_names()
'''print(dbs)'''
test_db = client.test
collections = test_db.list_collection_names()
print(collections)

def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Aisha",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

insert_test_doc()

production = client.production
person_collection = production.person_collection

def create_documents():
    first_names = ["Aisha","Omar","zaina","Atesh","Raihana","Adnan"]
    last_names = ["kay","Ray","Key","Achar","Urb","Shix"]
    ages = [70, 21, 23, 24, 50, 30]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)
    
    person_collection.insert_many(docs)

'''create_documents()'''

printer = pprint.PrettyPrinter()

def find_all_people():
    people = person_collection.find()
    ''''prints a cursor which something that is an iterable'''
    '''print(people)
    print(list(people))'''

    for person in people:
        printer.pprint(person)

'''find_all_people()'''

def find_Aisha():
    Aisha = person_collection.find_one({"first_name": "Aisha"})
    printer.pprint(Aisha)

find_Aisha()
    
def count_all_people():
    count = person_collection.count_documents(filter={})
    print("Number of people", count)

'''count_all_people()'''

def get_person_by_id(person_id):
    from bson.objectid import ObjectId
    
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)

get_person_by_id("64b5c71dea59630b0f817770")

def get_age_range(min_age, max_age):
    query = {"$and": [
        {"age": {"$gte": min_age}},
        {"age": {"$lte": max_age}}
    ]}

    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)

get_age_range(20,35)

