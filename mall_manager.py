from establishment import Establishment
from store import Store
import bulls_and_cows
import labyrinth
import deal_or_no_deal
import sudoku
import hangman


your_shoes = Store("your_shoes", "shoe_store", 152)
mimis_grocery = Store("mimis_grocery", "grocery", 150)
pythons_clothes = Store("pythons_clothes", "clothes_store", 150)
anakonda = Establishment("anakonda", "restaurant", 150)
ubuntu = Establishment("ubuntu", "cafe", 150)


def game_to_play(choice):
    if choice == 1:
        return bulls_and_cows.start()
    elif choice == 2:
        return labyrinth.start()
    elif choice == 3:
        return deal_or_no_deal.start()
    elif choice == 4:
        return sudoku.start()
    elif choice == 5:
        return hangman.start()
    else:
        print("Invalid command")


def game_room():
    print("Here are our games:")
    print("1 - bulls_and_cows")
    print("2 - labyrinth")
    print("3 - deal_or_no_deal")
    print("4 - sudoku")
    print("5 - hangman")
    print("7 - for exit!!")

    while True:
        print("Don't forget - input 7 for exit!!")
        choice = input("The game you want to play: ")
        choice = int(choice)
        if choice == 7:
            break
        else:
            game_to_play(choice)


def where_to_go(choice):
    if choice == 1:
        return your_shoes.enter()
    elif choice == 2:
        return mimis_grocery.enter()
    elif choice == 3:
        return pythons_clothes.enter()
    elif choice == 4:
        return anakonda.enter()
    elif choice == 5:
        return ubuntu.enter()
    elif choice == 6:
        return game_room()
    else:
        print("Invalid command")


def main():

    print("WELCOME TO THE MALL!!!")
    print("Here are our stores:")
    print("1 - your_shoes")
    print("2 - mimis_grocery")
    print("3 - pythons_clothes")
    print("4 - anakonda")
    print("5 - ubuntu")
    print("6 - game room")
    print("7 - for exit!!")

    while True:
        print("Don't forget - input 7 for exit!!")
        choice = input("Insert the number you would like to go to: ")
        choice = int(choice)
        if choice == 7:
            break
        else:
            where_to_go(choice)

if __name__ == '__main__':
    main()
