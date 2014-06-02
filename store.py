import store_sql_manager


class Store:
    def __init__(self, name, type, money):
        self._name = name
        self._type = type
        self._money = money

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def enter_the_store(self):
        print("Welcome to {} !".format(self.name))
        print("If you are part of the staff please insert 1")
        print("If you want to shop here please insert 2")

        choice = input("+++")
        if(choice == "1"):
            print("""For loading the sold out items insert 1,
                     for deleting the store insert 2
                     for adding items insert 3""")
            staff_choice = input("+++")
            if(staff_choice == "1"):
                quantity = input("quantity: ")
                store_sql_manager.load_items(quantity)

            elif(staff_choice == "2"):
                store_sql_manager.delete_store(self.name)

            elif(staff_choice == "3"):
                item = input("item: ")
                description = input("description: ")
                providers_price = input("provider's price: ")
                selling_price = input("selling price: ")
                quantity = input("quantity: ")

                store_sql_manager.add_item(self.name, item, description, providers_price, selling_price, quantity)

            else:
                print("invalid command")

        elif (choice == "2"):
            print("to see all the items in the store - 1")
            print("to see item with actual id - 2")
            print("to buy item - 3")
            buyer_choice = input("+++")
            if(buyer_choice == "1"):
                store_sql_manager.view_items()
            elif(buyer_choice == "2"):
                id = input("id: ")
                store_sql_manager.view_item(id)
            elif(buyer_choice == "3"):
                item = input("item you want to buy: ")
                store_sql_manager.sell_item(self.name, item)
                print("---you just bought {}---".format(item))
            else:
                print("invalid command")

        else:
            print("invalid command")
