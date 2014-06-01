import unittest
import store_sql_manager


class StoreSqlManagerTests(unittest.TestCase):

    def setUp(self):
        store_sql_manager.create_table()
        store_sql_manager.add_item("test_store", "bag", "color: pink", 23.4, 30, 5)
        store_sql_manager.add_item("test_store", "book", "pages: 241", 15, 21, 6)
        store_sql_manager.add_item("test_store2", "poison", "", 12, 56, 0)

    def tearDown(self):
        store_sql_manager.cursor.execute('DROP TABLE stores')

    def test_add_item(self):
        store_sql_manager.cursor.execute("SELECT Count(*) FROM stores WHERE name = ?", ("test_store",))
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 2)

    def test_get_quantity(self):
        result = store_sql_manager.get_quantity("test_store", "bag")
        self.assertEqual(5, result)

    def test_sell_item(self):
        store_sql_manager.sell_item("test_store", "bag")
        result = store_sql_manager.get_quantity("test_store", "bag")
        self.assertEqual(4, result)

    def test_view_items(self):
        self.assertTrue(store_sql_manager.view_items())

    def test_view_item(self):
        self.assertTrue(store_sql_manager.view_item(1))

    def test_view_item_with_invalid_id(self):
        self.assertFalse(store_sql_manager.view_item(4))

    def test_view_item_with_zero_quantity(self):
        self.assertFalse(store_sql_manager.view_item(3))

    def test_delete_store(self):
        store_sql_manager.delete_store("test_store2")
        store_sql_manager.cursor.execute("SELECT Count(*) FROM stores")
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 2)

    def test_load_items(self):
        store_sql_manager.load_items(2)
        result = store_sql_manager.get_quantity("test_store2", "poison")
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()
