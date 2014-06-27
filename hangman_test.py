from hangman import show_hangman
import unittest


class HangmanTest(unittest.TestCase):
    def test_show_hangman_one(self):
        self.assertEqual("\n \n|   \n|   \n|  \n|   \n", show_hangman(1))

    def test_show_hangman_two(self):
        self.assertEqual("\n ____\n|   \n|   \n|  \n|   \n", show_hangman(2))

    def test_show_hangman_three(self):
        self.assertEqual("\n ____\n|   |\n|   \n|  \n|   \n", show_hangman(3))

    def test_show_hangman_four(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|    \n|   \n",
                         show_hangman(4))

    def test_show_hangman_five(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|  /  \n|  \n",
                         show_hangman(5))

    def test_show_hangman_six(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|  / \ \n|   \n",
                         show_hangman(6))

    def test_show_hangman_seven(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|  /|\ \n|   \n",
                         show_hangman(7))

    def test_show_hangman_eight(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|  /|\ \n|  /  \n",
                         show_hangman(8))

    def test_show_hangman_nine(self):
        self.assertEqual("\n ____\n|   |\n|   O\n|  /|\ \n|  / \ \n",
                         show_hangman(9))

if __name__ == '__main__':
    unittest.main()
