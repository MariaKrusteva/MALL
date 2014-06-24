import establishment_sql_manager


class Establishment:
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

    @property
    def type(self):
        return self._type

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    def thirsty_or_hungry(self):
        if self.type == "cafe":
            print("sooo you are thirsty?")
        else:
            print("sooo you are hungry")

    def enter(self):

        print("Welcome to {} !".format(self.name))
        self.thirsty_or_hungry()

        while True:
            print("to see all the items insert 1")
            print("to see item with actual id insert 2")
            print("to buy item insert 3")
            print("if you want to exit insert 4")

            buyer_choice = input("+++")

            if buyer_choice == "1":
                establishment_sql_manager.view_items(self.name)

            elif buyer_choice == "2":
                id = input("id: ")
                establishment_sql_manager.view_item(self.name, id)

            elif buyer_choice == "3":
                item = input("item you want to buy: ")
                price = establishment_sql_manager.get_price(self.name, item)
                self.money += price
                print("---you just bought {}---".format(item))

            elif buyer_choice == "4":
                break

            else:
                print("invalid command")
