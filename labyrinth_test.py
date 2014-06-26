from labyrinth import (level_to_load,
                       get_number_of_rows,
                       get_number_of_columns,
                       finish,
                       make_a_move)
import labyrinth_maps
import unittest


class LabyrinthTest(unittest.TestCase):
    def test_level_to_load_one(self):
        self.assertEqual(level_to_load("1"), labyrinth_maps.level_one())

    def test_level_to_load_two(self):
        self.assertEqual(level_to_load("2"), labyrinth_maps.level_two())

    def test_level_to_load_three(self):
        self.assertEqual(level_to_load("3"), labyrinth_maps.level_three())

    def test_level_to_load_four(self):
        self.assertEqual(level_to_load("4"), labyrinth_maps.level_four())

    def test_level_to_load_five(self):
        self.assertEqual(level_to_load("5"), labyrinth_maps.level_five())

    def test_get_number_of_rows(self):
        self.assertEqual(2, get_number_of_rows("S...\n~~~F"))

    def test_get_number_of_rows_with_one_row_map(self):
        self.assertEqual(1, get_number_of_rows("S...~...~.~~F"))

    def test_get_number_of_rows_with_a_big_map(self):
        self.assertEqual(6, get_number_of_rows(
            "S.~~~...\n~...~~..\n~..~....\n.~~....~\n~..~~~..\n.......F"))

    def test_get_number_of_columns(self):
        self.assertEqual(4, get_number_of_columns("S...\n~~~F"))

    def test_get_number_of_rows_with_one_column_map(self):
        self.assertEqual(1, get_number_of_columns("S\n.\n.\nF"))

    def test_get_number_of_columns_with_a_big_map(self):
        self.assertEqual(8, get_number_of_columns(
            "S.~~~...\n~...~~..\n~..~....\n.~~....~\n~..~~~..\n.......F"))

    def test_finish(self):
        self.assertFalse(finish(0, 3, 2))

    def test_finish_false(self):
        self.assertFalse(finish(15, 6, 4))

    def test_finish_true(self):
        self.assertTrue(finish(26, 4, 6))

    def test_make_a_move(self):
        self.assertFalse(make_a_move(
            0,
            "l",
            labyrinth_maps.level_one(),
            get_number_of_rows(labyrinth_maps.level_one()),
            get_number_of_columns(labyrinth_maps.level_one())
        ))

    def test_an_invalid_move(self):
        self.assertFalse(make_a_move(
            0,
            "u",
            labyrinth_maps.level_one(),
            get_number_of_rows(labyrinth_maps.level_one()),
            get_number_of_columns(labyrinth_maps.level_one())
        ))

    def test_another_invalid_move(self):
        self.assertFalse(make_a_move(
            22,
            "d",
            labyrinth_maps.level_one(),
            get_number_of_rows(labyrinth_maps.level_one()),
            get_number_of_columns(labyrinth_maps.level_one())
        ))

    def test_once_more_invalid_move(self):
        self.assertFalse(make_a_move(
            5,
            "r",
            labyrinth_maps.level_one(),
            get_number_of_rows(labyrinth_maps.level_one()),
            get_number_of_columns(labyrinth_maps.level_one())
        ))

    def test_valid_move(self):
        result = make_a_move(
            0,
            "r",
            labyrinth_maps.level_one(),
            get_number_of_rows(labyrinth_maps.level_one()),
            get_number_of_columns(labyrinth_maps.level_one())
        )
        self.assertEqual("SO.~..\n.~....\n......\n..~..F", result[0])
        self.assertEqual(1, result[1])


if __name__ == '__main__':
    unittest.main()
