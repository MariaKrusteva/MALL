from deal_or_no_deal import calculate_bank_offer, the_last_price_left
import unittest


class DealOrNoDealTest(unittest.TestCase):
    def test_calculate_bank_offer(self):
        self.assertEqual(7, calculate_bank_offer([1, 2, 3, 4, 5]))

    def test_calculate_bank_offer_two(self):
        self.assertEqual(91, calculate_bank_offer([1, 2, 63, 4, 95, 18]))

    def test_calculate_bank_offer_three(self):
        self.assertEqual(101, calculate_bank_offer([15, 62, 63, 0, 95, 18]))

    def test_calculate_bank_offer_negative_result(self):
        self.assertEqual(3200, calculate_bank_offer([0, 0, 0, 0, 0, 0]))

    def test_the_last_price_left(self):
        self.assertEqual(2, the_last_price_left([0, 0, 0, 2]))

    def test_the_last_price_left_two(self):
        self.assertEqual(1, the_last_price_left([0, 0, 1, 0, 0]))

    def test_the_last_price_left_three(self):
        self.assertEqual(1200, the_last_price_left([0, 0, 0, 1200]))


if __name__ == '__main__':
    unittest.main()
