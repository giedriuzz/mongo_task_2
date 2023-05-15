import connect
from main import MongoDb
from pymongo.collection import Collection



# mongo config
mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'books'
collection_name = 'science_books'

mongo = MongoDb()
# connection
db = connect.connect_to_mongodb(mongodb_host, mongodb_port, database_name)
collection = db[collection_name]

document = {
    "task_name": "Wash car",
    "task_description": 'Wash car only with water',
    "task_status": "started",
    "user_name": "Tadas Tadas",
    "user_email": "tadas@gmail.com",
}
mongo.insert_create_document(collection=collection, document=document)

while True:
    selection = int(input("Select what to do: \n1 - Read \n2 - Create \n3 - Update \n4 - Delete \n5 - Exit\n"))

    if selection == 1:
        collections = mongo.get_database_collection(db, collection_name)
        print(collections)  

    if selection == 2:
        t_name = input("Please insert task name: ")
        t_deskription = input("Enter task description: ")
        t_status = input("Task status (ex.: 'not started'): ")
        u_name = input("User name: ")
        u_email = input("User email: ")
        in_task = {
            "task_name": t_name, 
            "task_description": t_deskription, 
            "task_status": t_status, 
            "user_name": u_name, 
            "user_email": u_email, 
        }
        task = mongo.insert_create_document(collection=collection, document=in_task)

        print(f"Task added with ID: {task}")

    if selection == 3:
        print("Would be Update")

    if selection == 4:
        print("Would be Delete")

    if selection == 5:
        exit()
    