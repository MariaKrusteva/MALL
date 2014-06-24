import store_sql_manager


class Store:
    def __init__(self, name, type, money):
        self._name = name
        self._type = type
        self._money = money

        store_sql_manager.add_staff_information(self.name,
                                                self.name + "123",
                                                "really987HARD654password")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    def is_part_of_the_staff(self):
        username = input("username: ")
        password = input("password: ")
        valid = store_sql_manager.get_staff_information(self.name)
        return username == valid[0] and password == valid[1]

    def staff_menu(self):
        print("for loading the sold out items insert 1")
        print("for deleting the store insert 2")
        print("for adding items insert 3")
        print("if you want to exit insert 4")

        staff_choice = input("+++")

        if staff_choice == "1":
            quantity = input("quantity: ")
            store_sql_manager.load_items(quantity)

        elif staff_choice == "2":
            store_sql_manager.delete_store(self.name)

        elif staff_choice == "3":
            item = input("item: ")
            description = input("description: ")
            providers_price = input("provider's price: ")
            selling_price = input("selling price: ")
            quantity = input("quantity: ")

            store_sql_manager.add_item(
                self.name,
                item,
                description,
                providers_price,
                selling_price,
                quantity
            )

        elif staff_choice == "4":
            return False

        else:
            print("invalid command")

        return True

    def buyer_menu(self):

        print("""to see all the items in the store insert 1
                 to see item with actual id insert 2
                 to buy item insert 3
                 if you want to exit insert 4""")

        buyer_choice = input("+++")

        if buyer_choice == "1":
            store_sql_manager.view_items(self.name)

        elif buyer_choice == "2":
            id = input("id: ")
            store_sql_manager.view_item(self.name, id)

        elif buyer_choice == "3":
            item = input("item you want to buy: ")
            store_sql_manager.sell_item(self.name, item)
            print("---you just bought {}---".format(item))
            price = store_sql_manager.get_price(self.name, item)
            self.money += price

        elif buyer_choice == "4":
            return False

        else:
            print("invalid command")

        return True

    def enter(self):
        print("Welcome to {} !".format(self.name))
        print("If you are part of the staff please insert 1")
        print("If you want to shop here please insert 2")
        print("If you want to leave please insert 3")

        choice = input("+++")

        if choice == "1":
            if self.is_part_of_the_staff():
                while True:
                    execute = self.staff_menu()
                    if not execute:
                        break
            else:
                print("YOU SHALL NOT PASS")

        elif choice == "2":
            while True:
                execute = self.buyer_menu()
                if not execute:
                    break

        elif choice == "3":
            print("you just left {}".format(self.name))
