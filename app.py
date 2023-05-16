import connect
from main import MongoDb
from pymongo.collection import Collection



# mongo config
mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'Tasks'
collection_name = 'user_tasks'

mongo = MongoDb(mongodb_host, mongodb_port, database_name, collection_name)
# connection
db = connect.connect_to_mongodb(mongodb_host, mongodb_port, database_name)
collection = db[collection_name]

# document = {
#     "task_name": "Wash car",
#     "task_description": 'Wash car only with water',
#     "task_status": "started",
#     "user_name": "Tadas Tadas",
#     "user_email": "tadas@gmail.com",
# }
# mongo.insert_create_document(collection=collection, document=document)

def create_new_task() -> None:
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
    task = mongo.insert_create_document(document=in_task)

    print(f"Task added with ID: {task}")  


def view_all_tasks():
    tasks = mongo.find_documents()
    print("Your tasks:")
    for task in tasks:
        print(f"ID: {task['_id']}")
        print(f"Task name: {task['task_name']}")
        print(f"Task description: {task['task_description']}")
        print(f"Task status: {task['task_status']}")
        print(f"User name: {task['user_name']}")
        print(f"User email: {task['user_email']}")
        print("**************************************************")


def update_task():
    task_id = input("Enter task ID: ")
    status = input("Enter task status: ")
    new_status = {"task_status": status}
    update_status = mongo.update_document(task_id, new_status)
    print(f"{update_status} task(s) updated.")

def delete_task():
    task_id = input("Enter task ID, which should be deleted: ")
    delete_count = mongo.delete_document(task_id)
    print(f"{task_id} task removed.")



while True:
    selection = int(input("Select what to do: \n1 - Read \n2 - Create \n3 - Update \n4 - Delete \n5 - Exit\n"))

    if selection == 1:
        view_all_tasks()

    if selection == 2:
        create_new_task()

    if selection == 3:
        update_task()

    if selection == 4:
        delete_task()

    if selection == 5:
        exit()
    