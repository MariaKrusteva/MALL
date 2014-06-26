from random import randint


def number_to_list(n):
    result = []
    while(n != 0):
        result.insert(0, n % 10)
        n = n // 10
    return result


def make_random_number():
    result = []
    for i in range(0, 4):
        x = randint(0, 9)
        result.append(x)
    return result


def check_for_bulls(assumption, number):
    """We don't want a digit which is bull to appear as a cow,
       it would cause confusion"""
    result = 0
    assumption = number_to_list(int(assumption))
    for i in range(0, 4):
        if assumption[i] == number[i]:
            assumption[i] = -1
            result += 1
    return (result, assumption)


def check_for_cows(assumption, number):
    result = 0
    for digit in assumption:
        if digit in number:
            result += 1
    return result


def start():
    print("Welcome to bulls and cows game!")
    attempts = input(
        "In how many attempts would you like to solve the number ?"
    )
    print("Dont forget to insert number with 4 digits")
    print("Here we go!")
    computer_number = make_random_number()
    print(computer_number)
    for i in range(0, int(attempts)):
        assumption = input("Your number: ")

        x = check_for_bulls(assumption, computer_number)
        bulls = x[0]
        cows = check_for_cows(x[1], computer_number)

        if bulls == 0:
            print("You have {} cows".format(cows))
        elif cows == 0:
            print("You have {} bulls".format(bulls))
        elif bulls == 4:
            print("YOU WIN")
            break
        else:
            print("You have {} cows and {} bulls".format(cows, bulls))

    if i == int(attempts) - 1:
        print("your number was {}".format(computer_number))
