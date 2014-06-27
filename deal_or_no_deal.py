from random import randint
PRICES = [10,
          20,
          50,
          100,
          250,
          300,
          500,
          700,
          1000,
          2500,
          3000,
          5000,
          7500,
          10000,
          15000,
          50000,
          100000]


def allocate_money():
    result = []
    for i in range(0, 17):
        index = randint(0, 16)

        while PRICES[index] == 0:
            index = randint(0, 16)

        result.append(PRICES[index])
        PRICES[index] = 0
    return result


def calculate_bank_offer(boxes):
    result = 0
    if boxes.count(100000) == 0:
        result = int((sum(boxes) - boxes.count(0) * 50) / 2)
    else:
        result = int((sum(boxes) - boxes.count(0) * 50 - 100000) / 2)

    if result <= 0:
        return 3200
    else:
        return result


def the_last_price_left(boxes):
    """We are sure there is ony one price different from zero"""
    i = 0
    while boxes[i] == 0:
        i += 1
    return boxes[i]


def start():
    print("Welcome to Deal or no Deal!")
    print("Don't forget to pick e box between 1 and 17")
    boxes = allocate_money()
    chosen_index = int(input("Your box will be number: "))
    chosen_box = boxes[chosen_index - 1]
    boxes[chosen_index - 1] = 0
    i = 0
    while i < 15:
        chosen_index = int(input("The box you want to open: "))
        if boxes[chosen_index - 1] == 0:
            print("That box is open!")
        else:
            print("Box number {} contains {} money".format(
                chosen_index,
                boxes[chosen_index - 1]
            ))

            boxes[chosen_index - 1] = 0
            i += 1

        if i % 3 == 0 and i != 0:
            bank_money = calculate_bank_offer(boxes)
            print("Bank's offer is {}".format(bank_money))
            decision = input("input yes for deal and no for no deal: ")
            if decision == "yes":
                print("You win {} money".format(bank_money))
                break
            else:
                print("NO DEAL, we're continuing")

    if i == 15:
        decision = input("Do you want a change? (y/n) :")
        if decision == "y":
            new_box = the_last_price_left(boxes)
            print("You are winning {} money".format(new_box))
            print("In your privious box were {} money".format(chosen_box))
        else:
            print("You're winning {} money".format(chosen_box))

    else:
        print("In your box there were {} money".format(chosen_box))
