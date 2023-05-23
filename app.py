from connect import connect
from main import MongoDb
from pymongo.collection import Collection


# mongo config
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "raspberryDb"
collection_name = "raspberryCol"

mongo = MongoDb()
# connection
db = connect.Connect().connect_to_mongodb(mongodb_host, mongodb_port, database_name)
collection = db[collection_name]

# --- insert
document = {"name": "Pilsutskis Marius", "age": 15, "email": "pilsustskis@gmail.com"}
mongo.insert_create_document(collection=collection, document=document)

# document = {
#     "task_name": "Wash car",
#     "task_description": "Wash car only with water",
#     "task_status": "started",
#     "user_name": "Tadas Tadas",
#     "user_email": "tadas@gmail.com",
# }
# mongo.insert_create_document(collection=collection, document=document)

# # Read
# query = {"age": 15}
# results = mongo.find_documents(collection=collection, query=query)
# print(results)


# get collections
collections = mongo.get_database_collection(db, collection_name)
for c in collections:
    print(c)
