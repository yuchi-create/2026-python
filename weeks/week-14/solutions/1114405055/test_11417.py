# test_11417.py - UVA 11417 測試程式
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "11417.py"


def run(input_text):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class TestGcdSum(unittest.TestCase):
    def test_sample(self):
        """題目給的範例測資"""
        input_text = "10\n100\n500\n0\n"
        expected = "67\n13015\n442011"
        self.assertEqual(run(input_text), expected)

    def test_minimum_n(self):
        """N = 2 時只有一對 (1, 2)，gcd(1,2) = 1"""
        input_text = "2\n0\n"
        expected = "1"
        self.assertEqual(run(input_text), expected)


if __name__ == "__main__":
    unittest.main()
