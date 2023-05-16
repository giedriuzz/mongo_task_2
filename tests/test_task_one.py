import unittest
from connect.connect import Connect
from main import MongoDb
from pymongo import MongoClient


class UnitTestsOfMain(unittest.TestCase):
    def setUp(self):
        self.mongo = MongoDb()
        self.mongodb_host = "localhost"
        self.mongodb_port = 27017
        self.database_name = "Tasks"
        self.collection_name = "user_tasks"
        connects = Connect()
        # connection
        self.db = connects.connect_to_mongodb(
            self.mongodb_host, self.mongodb_port, self.database_name
        )
        self.collection = self.db[self.collection_name]

        self.query = {"task_name": "Wash car"}
        self.update = {"task_name": "Not wash a car, wash a bike"}
        self.client = MongoClient(self.mongodb_host, self.mongodb_port)

    def test_insert_create_document(self):
        result = {
            "task_name": "Wash car",
            "task_description": "Wash car only with water",
            "task_status": "started",
            "user_name": "Tadas Tadas",
            "user_email": "tadas@gmail.com",
        }
        self.assertIsNotNone(self.mongo.insert_create_document(self.collection, result))

    def test_find_documents(self):
        self.assertIsNotNone(self.mongo.find_documents(self.collection, self.query))

    def test_update_document(self):
        self.assertIsNotNone(
            self.mongo.update_document(self.collection, self.query, self.update)
        )
        self.assertGreaterEqual(
            self.mongo.update_document(self.collection, self.query, self.update), 0
        )

    def test_delete_documents(self):
        self.assertGreaterEqual(
            self.mongo.delete_documents(self.collection, self.update), 0
        )

    def test_get_database_collection(self):
        collection_name = "fake"
        fake_collection = self.db[collection_name]
        self.assertEqual(
            self.mongo.get_database_collection(self.db, self.collection_name),
            self.collection,
        )
        with self.assertRaises(TypeError):
            self.mongo.get_database_collection(self.db, fake_collection)  # type:ignore

    def test_list_databases(self):
        self.assertIsNotNone(self.mongo.list_databases(self.client))

    def test_list_collections(self):
        self.assertIsNotNone(self.mongo.list_collections(self.db))  # type:ignore
