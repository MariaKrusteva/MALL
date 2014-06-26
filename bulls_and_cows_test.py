from bulls_and_cows import number_to_list, check_for_cows, check_for_bulls
import unittest


class BullsAndCowsTest(unittest.TestCase):
    def test_number_to_list_one(self):
        self.assertEqual([1, 2, 3], number_to_list(123))

    def test_number_to_list_two(self):
        self.assertEqual([9, 9, 9, 9, 9], number_to_list(99999))

    def test_number_to_list_three(self):
        self.assertEqual([1, 2, 3, 0, 2, 3], number_to_list(123023))

    def test_check_for_cows(self):
        self.assertEqual(2, check_for_cows([1, 2, 3, 4], [4, 3, 0, 0]))

    def test_check_for_cows_with_no_coincidence(self):
        self.assertEqual(0, check_for_cows([1, 2, 3, 4], [7, 8, 9, 0]))

    def test_check_for_cows_with_the_same_number(self):
        self.assertEqual(4, check_for_cows([4, 5, 6, 9], [4, 5, 6, 9]))

    def test_check_for_bulls(self):
        x = check_for_bulls("1340", [4, 3, 0, 0])
        self.assertEqual(2, x[0])
        self.assertEqual([1, -1, 4, -1], x[1])

    def test_check_for_bulls_with_no_coincidence(self):
        x = check_for_bulls("9708", [7, 8, 9, 0])
        self.assertEqual(0, x[0])
        self.assertEqual([9, 7, 0, 8], x[1])

    def test_check_for_bulls_with_the_same_number(self):
        x = check_for_bulls("4561", [4, 5, 6, 1])
        self.assertEqual(4, x[0])
        self.assertEqual([-1, -1, -1, -1], x[1])

if __name__ == '__main__':
    unittest.main()
