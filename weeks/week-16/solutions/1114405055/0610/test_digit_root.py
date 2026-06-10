"""數字根 — 測試

題目：digit_root(n) 反覆把 n 的各位數字相加，直到剩一位數，回傳該一位數。
      若 n < 1，應 raise ValueError("n must be >= 1")。
"""

import unittest

from digit_root import digit_root


class TestDigitRoot(unittest.TestCase):
    def test_basic_multi_step(self):
        # 199 → 1+9+9=19 → 1+9=10 → 1+0=1
        self.assertEqual(digit_root(199), 1)

    def test_basic_single_step(self):
        # 24 → 2+4=6
        self.assertEqual(digit_root(24), 6)

    def test_basic_nine(self):
        # 9999 → 36 → 9
        self.assertEqual(digit_root(9999), 9)

    def test_edge_single_digit(self):
        # 已是一位數，直接回傳自己
        self.assertEqual(digit_root(5), 5)
        self.assertEqual(digit_root(1), 1)
        self.assertEqual(digit_root(9), 9)

    def test_edge_large_number(self):
        # 上限值 2,000,000,000 → 2+0+...= 2
        self.assertEqual(digit_root(2_000_000_000), 2)

    def test_invalid_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(0)
        self.assertEqual(str(ctx.exception), "n must be >= 1")

    def test_invalid_negative_raises(self):
        with self.assertRaises(ValueError) as ctx:
            digit_root(-5)
        self.assertEqual(str(ctx.exception), "n must be >= 1")


if __name__ == "__main__":
    unittest.main()
