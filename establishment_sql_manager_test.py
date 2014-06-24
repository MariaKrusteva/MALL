import unittest
import establishment_sql_manager


class EstablishmentSqlManagerTess(unittest.TestCase):

    def setUp(self):
        establishment_sql_manager.create_table()
        establishment_sql_manager.add_item("test_cafe",
                                           "cafe",
                                           "tea",
                                           "teabag , water, honey",
                                           2.3,
                                           250)

        establishment_sql_manager.add_item("test_restaurant",
                                           "restaurant",
                                           "pizza",
                                           "tomato sauce, cheese, ham, olives",
                                           5.6,
                                           400)

        establishment_sql_manager.add_item("test_restaurant",
                                           "restaurant",
                                           "bread",
                                           "",
                                           0.4,
                                           20)

    def tearDown(self):
        establishment_sql_manager.cursor.execute('DROP TABLE establishments')

    def test_add_item_restaurant(self):
        select_query = "SELECT Count(*) FROM establishments WHERE name = ?"
        establishment_sql_manager.cursor.execute(select_query,
                                                ("test_restaurant",))
        items_count = establishment_sql_manager.cursor.fetchone()

        self.assertEqual(2, items_count[0])

    def test_add_item_cafe(self):
        select_query = "SELECT Count(*) FROM establishments WHERE name = ?"
        establishment_sql_manager.cursor.execute(select_query, ("test_cafe",))
        items_count = establishment_sql_manager.cursor.fetchone()

        self.assertEqual(1, items_count[0])

    def test_add_another_item(self):
        establishment_sql_manager.add_item("test",
                                           "cafe",
                                           "2 in 1",
                                           "instant coffee, sugar",
                                           1.6,
                                           20)
        select_query = "SELECT Count(*) FROM establishments WHERE name = ?"
        establishment_sql_manager.cursor.execute(select_query,
                                                ("test_restaurant",))
        items_count = establishment_sql_manager.cursor.fetchone()

        self.assertEqual(2, items_count[0])

    def test_view_items(self):
        self.assertTrue(establishment_sql_manager.view_items(
            "test_restaurant")
        )

    def test_get_price_of_pizza(self):
        result = establishment_sql_manager.get_price("test_restaurant",
                                                     "pizza")
        self.assertEqual(5.6, result)

    def test_get_price_of_bread(self):
        result = establishment_sql_manager.get_price("test_restaurant",
                                                     "bread")
        self.assertEqual(0.4, result)

    def test_get_price_of_tea(self):
        result = establishment_sql_manager.get_price("test_cafe", "tea")
        self.assertEqual(2.3, result)

    def test_view_item(self):
        self.assertTrue(establishment_sql_manager.view_item("test_cafe", 1))

    def test_view_item_with_invalid_id(self):
        self.assertFalse(establishment_sql_manager.view_item("test_cafe", 4))

    def test_delete_establishment(self):
        establishment_sql_manager.delete_establishment("test_cafe")
        establishment_sql_manager.cursor.execute(
            "SELECT Count(*) FROM establishments"
        )
        items_count = establishment_sql_manager.cursor.fetchone()

        self.assertEqual(2, items_count[0])

    def test_delete_the_other_establishment(self):
        establishment_sql_manager.delete_establishment("test_restaurant")
        establishment_sql_manager.cursor.execute(
            "SELECT Count(*) FROM establishments"
        )
        items_count = establishment_sql_manager.cursor.fetchone()

        self.assertEqual(1, items_count[0])

if __name__ == '__main__':
    unittest.main()
