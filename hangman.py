from random import randint
WORDS = ["python", "project", "sublime", "linux"]


def show_hangman(step):
    if step == 1:
        return "\n \n|   \n|   \n|  \n|   \n"
    elif step == 2:
        return "\n ____\n|   \n|   \n|  \n|   \n"
    elif step == 3:
        return "\n ____\n|   |\n|   \n|  \n|   \n"
    elif step == 4:
        return "\n ____\n|   |\n|   O\n|    \n|   \n"
    elif step == 5:
        return "\n ____\n|   |\n|   O\n|  /  \n|  \n"
    elif step == 6:
        return "\n ____\n|   |\n|   O\n|  / \ \n|   \n"
    elif step == 7:
        return "\n ____\n|   |\n|   O\n|  /|\ \n|   \n"
    elif step == 8:
        return "\n ____\n|   |\n|   O\n|  /|\ \n|  /  \n"
    elif step == 9:
        return "\n ____\n|   |\n|   O\n|  /|\ \n|  / \ \n"


def choose_random_word():
    index = randint(0, len(WORDS) - 1)
    return WORDS[index]


def start():
    print("Welcome to hangman game!")
    word = choose_random_word()
    print("Here is your word: ")
    word_guess = "~" * len(word)
    print(word_guess)
    mistakes = 0
    while True:
        letter = input("Your letter: ")
        if word.count(letter) == 0:
            mistakes += 1
            print(show_hangman(mistakes))
        else:
            index = word.index(letter)
            word_guess = word_guess[:index] + letter + word_guess[index + 1:]
            print(word_guess)

        if mistakes == 9:
            print("Better luck next time!")
            break

        if word_guess == word:
            print("Good job! You win!")
            break
