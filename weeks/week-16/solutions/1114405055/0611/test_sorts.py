"""Stage 2 — 排序正確性測試（三種排序共用同一組測試）

Stage 3 的加速版直接 append 進 SORT_FUNCTIONS 即可吃到同一組測試。
"""

import random
import unittest

from sorts import bubble_sort, merge_sort, quick_sort

SORT_FUNCTIONS = [bubble_sort, quick_sort, merge_sort]


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            ([3, 1, 2], [1, 2, 3]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1], [1]),
            ([2, 2], [2, 2]),
        ]
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                for data, expected in cases:
                    self.assertEqual(sort_fn(data), expected)

    def test_empty_list(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn([]), [])

    def test_already_sorted(self):
        data = list(range(1, 11))
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn(data), data)

    def test_reverse_sorted(self):
        data = list(range(10, 0, -1))
        expected = list(range(1, 11))
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn(data), expected)

    def test_duplicates(self):
        data = [3, 1, 3, 2, 1, 3]
        expected = [1, 1, 2, 3, 3, 3]
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn(data), expected)

    def test_random_data_matches_builtin(self):
        rng = random.Random(42)
        data = [rng.randint(-1000, 1000) for _ in range(200)]
        expected = sorted(data)
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn(data), expected)

    def test_input_not_mutated(self):
        """回傳新 list，不可修改傳入的 list"""
        original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                data = list(original)
                sort_fn(data)
                self.assertEqual(data, original,
                                 f"{sort_fn.__name__} 修改了傳入的 list")

    def test_single_element_list(self):
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn([99]), [99])

    def test_all_same_elements(self):
        data = [7] * 10
        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(fn=sort_fn.__name__):
                self.assertEqual(sort_fn(data), data)


if __name__ == "__main__":
    unittest.main()
