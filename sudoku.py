import sudoku_loader


def level_to_load(gamer_choice):
    gamer_choice = int(gamer_choice)
    if gamer_choice == 1:
        return sudoku_loader.easy_level()
    elif gamer_choice == 2:
        return sudoku_loader.medium_level()
    elif gamer_choice == 3:
        return sudoku_loader.hard_level()
    elif gamer_choice == 4:
        return sudoku_loader.extreme_level()
    elif gamer_choice == 5:
        return sudoku_loader.unsolvable_level()


def is_square_correct(start_possition_row, start_possition_col, sudoku):
    sum = 0
    for i in range(start_possition_row, start_possition_row + 3):
        for j in range(start_possition_col, start_possition_col + 3):
            sum += sudoku[i][j]
    return sum == 45


def is_sudoku_solved(sudoku):
    total = 0

    for row in sudoku:
        if sum(row) != 45:
            return False

    for i in range(0, 9):
        for j in range(0, 9):
            total += sudoku[i][j]
        if total != 45:
            return False
        total = 0

    return (is_square_correct(0, 0, sudoku) and
            is_square_correct(0, 3, sudoku) and
            is_square_correct(0, 6, sudoku) and
            is_square_correct(3, 0, sudoku) and
            is_square_correct(3, 3, sudoku) and
            is_square_correct(3, 6, sudoku) and
            is_square_correct(6, 0, sudoku) and
            is_square_correct(6, 3, sudoku) and
            is_square_correct(6, 6, sudoku))


def print_sudoku(sudoku):
    for row in sudoku:
        print(row)


def start():
    print("Welcome to sudoku game!")
    print("Insert 1 for easy level")
    print("Insert 2 for medium level")
    print("Insert 3 for hard level")
    print("Insert 4 for extreme level")
    print("Insert 5 for unsolvable level")
    gamer_choice = input("Your choice: ")
    sudoku = level_to_load(gamer_choice)
    print_sudoku(sudoku)
    print("When sudoku is filled - insert 99, in row,column index and number")

    while True:
        row_index = int(input("Row index: "))
        column_index = int(input("Column index: "))
        number = int(input("Number: "))
        if row_index == 99 or column_index == 99 or number == 99:
            if is_sudoku_solved(sudoku):
                print("Congatulations! Your sudoku is perfect!")
            else:
                print("There is something wrong with your sudoku :(")
            break
        else:
            sudoku[row_index - 1][column_index - 1] = number
            print_sudoku(sudoku)
