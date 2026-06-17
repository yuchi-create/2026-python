import unittest

from gcd import sum_of_gcd


class TestSumOfGcd(unittest.TestCase):
    def test_n_equals_1_returns_zero(self):
        self.assertEqual(sum_of_gcd(1), 0)

    def test_n_equals_2(self):
        self.assertEqual(sum_of_gcd(2), 1)

    def test_n_equals_3(self):
        self.assertEqual(sum_of_gcd(3), 3)

    def test_n_equals_10(self):
        self.assertEqual(sum_of_gcd(10), 67)


if __name__ == "__main__":
    unittest.main()
