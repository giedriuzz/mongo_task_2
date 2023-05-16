import unittest
from connect.connect import Connect
from main import MongoDb


class UnitTestsOfMain(unittest.TestCase):
    def setUp(self):
        self.mongo = MongoDb()
        mongodb_host = "localhost"
        mongodb_port = 27017
        database_name = "Tasks"
        collection_name = "user_tasks"
        connects = Connect()
        # connection
        db = connects.connect_to_mongodb(mongodb_host, mongodb_port, database_name)
        self.collection = db[collection_name]

    def test_insert_create_document(self):
        result = {
            "task_name": "Wash car",
            "task_description": "Wash car only with water",
            "task_status": "started",
            "user_name": "Tadas Tadas",
            "user_email": "tadas@gmail.com",
        }
        self.assertIsNotNone(self.mongo.insert_create_document(self.collection, result))


# def test_sum_of_list(self):
#     self.assertEqual(self.task.sum_of_list([120, 1, 5, 2, 2]), 130)
#     self.assertNotEqual(self.task.sum_of_list([120, 1, 45, 78, 96]), 121)
#     with self.assertRaises(TypeError):
#         self.task.sum_of_list([14, 185, "14"])  # type:ignore

# def test_max_value(self):
#     self.assertEqual(self.task.max_value(14, 1444, 145, 45), 1444)
#     self.assertNotIn(self.task.max_value(14), [25, 45])
#     self.assertGreater(self.task.max_value(14, 12, 17), 10)

# def test_reversing_string(self):
#     self.assertEqual(self.task.reversing_string("hello"), "olleh")
#     self.assertNotEqual(self.task.reversing_string("hello"), "hello")

# def test_info_about_sentence(self):
#     self.assertEqual(self.task.info_about_sentence("He11o   World!"), (2, 6, 2, 2))
#     with self.assertRaises(TypeError):
#         self.task.info_about_sentence(1452587)  # type:ignore

# def test_unique_only(self):
#     self.assertEqual(self.task.unique_only(1, 2, 3, 3), ([1, 2, 3]))
#     self.assertIsNot(self.task.unique_only(4), 1)

# def test_is_it_prime_number(self):
#     self.assertEqual(self.task.is_it_prime_number(7), True)
#     self.assertEqual(self.task.is_it_prime_number(8), False)
#     self.assertFalse(self.task.is_it_prime_number(0), False)
#     with self.assertRaises(TypeError):
#         self.task.is_it_prime_number("1452587")  # type:ignore

# def test_reversed_sentence(self):
#     self.assertEqual(self.task.reversed_sentence("Hello World!"), "World! Hello")
#     self.assertIsNot(self.task.reversed_sentence("Hello World!"), "Hello World!")
#     self.assertNotEqual(self.task.reversed_sentence("Hello World!"), "Hello World!")

# def test_is_leap(self):
#     self.assertEqual(self.task.is_leap(2000), True)
#     self.assertNotEqual(self.task.is_leap(2010), True)
#     self.assertFalse(self.task.is_leap(2100), False)
#     with self.assertRaises(TypeError):
#         self.task.is_leap("1452587")  # type:ignore

# @freeze_time("2023-05-09")
# def test_check_data(self):
#     fake_data: str = "2000-01-01"
#     self.assertEqual(self.task.check_data(fake_data), datetime.timedelta(days=8529))
#     self.assertEqual(
#         ((self.task.check_data(fake_data) // 365)),
#         datetime.timedelta(days=23, seconds=31719, microseconds=452054),
#     )
