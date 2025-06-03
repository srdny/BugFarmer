import unittest
# Assuming 'my_database_module' handles database connections
# import my_database_module

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        # This method is called before EACH test method
        # Establish a database connection, create a test table, insert initial data
        print("\nSetting up database connection...")
        # self.db_connection = my_database_module.connect()
        # self.db_connection.execute("CREATE TABLE users (id INTEGER, name TEXT)")
        # self.db_connection.execute("INSERT INTO users VALUES (1, 'Alice')")
        self.users = [{"id": 1, "name": "Alice"}] # Simulate in-memory data

    def tearDown(self):
        # This method is called after EACH test method
        # Close the database connection, drop test tables, clean up
        print("Tearing down database connection...")
        # self.db_connection.close()
        self.users = [] # Clean up simulated data

    def test_get_user_by_id(self):
        print("Running test_get_user_by_id")
        # user = self.db_connection.query("SELECT * FROM users WHERE id=1")
        user = next((u for u in self.users if u["id"] == 1), None)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Alice")

    def test_add_new_user(self):
        print("Running test_add_new_user")
        # self.db_connection.execute("INSERT INTO users VALUES (2, 'Bob')")
        # new_user = self.db_connection.query("SELECT * FROM users WHERE id=2")
        self.users.append({"id": 2, "name": "Bob"})
        new_user = next((u for u in self.users if u["id"] == 2), None)
        self.assertIsNotNone(new_user)
        self.assertEqual(new_user["name"], "Bob")
        self.assertEqual(len(self.users), 2) # Check the size after adding

if __name__ == '__main__':
    unittest.main()