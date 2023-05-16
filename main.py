from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List, Any

class MongoDb:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        
    # Create(Insert)
    def insert_create_document(self, document: Dict) -> str:
        result = self.collection.insert_one(document)
        return str(result.inserted_id)
    
    # Read
    def find_documents(self) -> List[Dict[str, Any]]:
        # documents = self.collection.find_one(query)
        return list(self.collection.find())
    
    # Update
    def update_document(self, task_id: str, status: Dict[str, Any]) -> int:
        result = self.collection.update_one({"_id": task_id}, {"$set": status})
        return result.modified_count
    
    # Delete
    def delete_document(self, task_id: str) -> int:
        result = self.collection.delete_one({'_id': task_id})
        return result.deleted_count
    
    def delete_documents(self, query: Dict) -> int:
        result = self.collection.delete_many(query)
        return result.deleted_count
    
    def get_database_collection(self, database: Database, collection_name: str) -> Collection:
        collection = database[collection_name]
        return list(collection.find())

    def list_databases(self, client: MongoClient) -> List[str]:
        return client.list_database_names()

    def list_collections(self, database: Database) -> List[str]:
        return database.list_collection_names()