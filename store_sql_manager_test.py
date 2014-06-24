import unittest
import store_sql_manager


class StoreSqlManagerTests(unittest.TestCase):

    def setUp(self):
        store_sql_manager.create_table()
        store_sql_manager.create_staff_table()
        store_sql_manager.add_item("test_store",
                                   "bag",
                                   "color: pink",
                                   23.4,
                                   30,
                                   5)
        store_sql_manager.add_item("test_store",
                                   "book",
                                   "pages: 241",
                                   15,
                                   21,
                                   6)
        store_sql_manager.add_item("test_store2", "poison", "", 12, 56, 0)

    def tearDown(self):
        store_sql_manager.cursor.execute('DROP TABLE stores')
        store_sql_manager.cursor.execute('DROP TABLE staff')

    def test_add_item(self):
        select_query = "SELECT Count(*) FROM stores WHERE name = ?"
        store_sql_manager.cursor.execute(select_query, ("test_store",))
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 2)

    def test_add_item_with_second_store(self):
        select_query = "SELECT Count(*) FROM stores WHERE name = ?"
        store_sql_manager.cursor.execute(select_query, ("test_store2",))
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 1)

    def test_get_quantity_of_the_bags(self):
        result = store_sql_manager.get_quantity("test_store", "bag")
        self.assertEqual(5, result)

    def test_get_quantity_of_the_books(self):
        result = store_sql_manager.get_quantity("test_store", "book")
        self.assertEqual(6, result)

    def test_get_price_of_book(self):
        result = store_sql_manager.get_price("test_store", "book")
        self.assertEqual(21, result)

    def test_sell_one_bag(self):
        store_sql_manager.sell_item("test_store", "bag")
        result = store_sql_manager.get_quantity("test_store", "bag")
        self.assertEqual(4, result)

    def test_sell_more_bags(self):
        store_sql_manager.sell_item("test_store", "bag")
        store_sql_manager.sell_item("test_store", "bag")
        result = store_sql_manager.get_quantity("test_store", "bag")
        self.assertEqual(3, result)

    def test_view_items(self):
        self.assertTrue(store_sql_manager.view_items("test_store"))

    def test_view_item(self):
        self.assertTrue(store_sql_manager.view_item("test_store", 1))

    def test_view_item_with_invalid_id(self):
        self.assertFalse(store_sql_manager.view_item("test_store2", 4))

    def test_view_item_with_zero_quantity(self):
        self.assertFalse(store_sql_manager.view_item("test_store2", 3))

    def test_delete_store(self):
        store_sql_manager.delete_store("test_store2")
        store_sql_manager.cursor.execute("SELECT Count(*) FROM stores")
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 2)

    def test_delete_the_other_store(self):
        store_sql_manager.delete_store("test_store")
        store_sql_manager.cursor.execute("SELECT Count(*) FROM stores")
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(items_count[0], 1)

    def test_load_items(self):
        store_sql_manager.load_items(2)
        result = store_sql_manager.get_quantity("test_store2", "poison")
        self.assertEqual(2, result)

    def test_load_items_one_more_time(self):
        store_sql_manager.add_item("test_store2", "eggs", "", 12, 56, 0)
        store_sql_manager.load_items(5)
        result = store_sql_manager.get_quantity("test_store2", "eggs")
        self.assertEqual(5, result)

    def test_add_staff_information_penka(self):
        store_sql_manager.add_staff_information("test", "penka", "p1e2n3k4a5")
        store_sql_manager.cursor.execute("SELECT Count(*) FROM staff")
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(1, items_count[0])

    def test_add_staff_information_penka_and_mitko(self):
        store_sql_manager.add_staff_information("test", "penka", "p1e2n3k4a5")
        store_sql_manager.add_staff_information("test", "mitko", "mitko56")
        store_sql_manager.cursor.execute("SELECT Count(*) FROM staff")
        items_count = store_sql_manager.cursor.fetchone()

        self.assertEqual(2, items_count[0])

    def test_get_staff_information(self):
        store_sql_manager.add_staff_information("test", "penka", "p1e2n3k4a5")
        result = ("penka", "p1e2n3k4a5")
        self.assertEqual(
            result,
            store_sql_manager.get_staff_information("test")
        )


if __name__ == '__main__':
    unittest.main()
