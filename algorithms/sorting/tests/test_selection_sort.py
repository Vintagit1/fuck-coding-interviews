# coding: utf-8
import unittest


from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.selection_sort import selection_sort_nested_for_loop


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(selection_sort(array.copy()), sorted(array))


class TestCase2(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(selection_sort_nested_for_loop(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()