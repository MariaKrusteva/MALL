from labyrinth_maps import (level_one,
                            level_two,
                            level_three,
                            level_four,
                            level_five)


def level_to_load(gamer_choice):
    gamer_choice = int(gamer_choice)
    if gamer_choice == 1:
        return level_one()
    elif gamer_choice == 2:
        return level_two()
    elif gamer_choice == 3:
        return level_three()
    elif gamer_choice == 4:
        return level_four()
    elif gamer_choice == 5:
        return level_five()


def get_number_of_rows(map):
    return map.count("\n") + 1


def get_number_of_columns(map):
    """We are sure the matrixes are square"""
    return map.index("\n")


def make_a_move(current_possition,
                direction,
                current_map,
                number_of_rows,
                number_of_columns):
    if direction == "u":
        if current_possition < number_of_columns:
            return False
        else:
            current_possition -= number_of_columns + 1
    elif direction == "d":
        if current_possition > (number_of_rows - 1) * (number_of_columns + 1):
            return False
        else:
            current_possition += number_of_columns + 1
    elif direction == "l":
        if current_possition % (number_of_columns + 1) == 0:
            return False
        else:
            current_possition -= 1
    elif direction == "r":
        if current_map[current_possition + 1] == "\n":
            return False
        else:
            current_possition += 1
    else:
        print("Invalid command")

    if current_map[current_possition] == "~":
        return False

    current_map = (current_map[:current_possition] +
                   "O" + current_map[current_possition + 1:])
    return (current_map, current_possition)


def finish(current_possition, number_of_rows, number_of_columns):
    final_cell = number_of_columns * number_of_rows + number_of_rows - 2
    return current_possition == final_cell


def start():
    print("Welcome to the Labyrinth game!")

    gamer_choice = input("Choose a level between 1 and 5: ")
    current_map = level_to_load(gamer_choice)
    number_of_rows = get_number_of_rows(current_map)
    number_of_columns = get_number_of_columns(current_map)
    current_possition = 0

    print(current_map)
    print("\nDon't forget\n~ means you can't move there\n. means you can")
    print("S stands for start and F for finish")
    print("O means you are here\nInsert u if you want to go up\nd for down")
    print("l for going left\nr for going right\ne for exit")

    while True:
        direction = input("Insert direction ")
        if direction == "e":
            break

        can_move = make_a_move(current_possition,
                               direction,
                               current_map,
                               number_of_rows,
                               number_of_columns)
        if can_move:
            current_map = can_move[0]
            current_possition = can_move[1]
            print(current_map)
        else:
            print("WHOOOPS you can't go there")

        if finish(current_possition, number_of_rows, number_of_columns):
            print("You win!")
            break
