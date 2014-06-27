import establishment_sql_manager
import store_sql_manager


def main():
    establishment_sql_manager.create_table()
    store_sql_manager.create_table()
    store_sql_manager.create_staff_table()

    stores = [("your_shoes", "snikers", "purple", 48, 52.3, 4),
              ("your_shoes", "high heels", "12cm", 65, 70, 5),
              ("your_shoes", "sandals", "brown", 23, 26, 5),
              ("mimis_grocery", "cheese", "white", 10, 12, 4),
              ("mimis_grocery", "bread", "700gr", 0.6, 1.2, 12),
              ("mimis_grocery", "sugar", "1kg", 1.2, 2, 13),
              ("pythons_clothes", "jeans", "blue", 35, 40.5, 7),
              ("pythons_clothes", "T-shirt", "green", 15, 20.3, 7),
              ("pythons_clothes", "skirt", "pleated", 23, 26, 7),
              ]

    establishments = [("anakonda", "restaurant", "sweet potatoes",
                       "potatoes herbs", 3.2, 350),
                      ("anakonda", "restaurant", "pizza", "cheese, tomatoes",
                       7.2, 400),
                      ("anakonda", "restaurant", "salad", "cucumber, tomato",
                       3.5, 350),
                      ("ubuntu", "cafe", "tea", "teabag, honey", 1.2, 250),
                      ("ubuntu", "cafe", "latte", " espresso, steamed milk",
                       2.5, 150),
                      ("ubuntu", "cafe", "latte", " espresso, steamed milk",
                       2.5, 150)]
    for store in stores:
        store_sql_manager.add_item(*store)

    for establishment in establishments:
        establishment_sql_manager.add_item(*establishment)

if __name__ == '__main__':
    main()
