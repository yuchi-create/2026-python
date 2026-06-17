# test_11461.py - UVA 11461 測試程式
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "11461.py"


def run(input_text):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class TestSquareNumbers(unittest.TestCase):
    def test_sample(self):
        """題目給的範例測資"""
        input_text = "1 4\n1 10\n1 100000\n0 0\n"
        expected = "2\n3\n316"
        self.assertEqual(run(input_text), expected)

    def test_single_square(self):
        """a == b 且恰好是完全平方數"""
        input_text = "9 9\n0 0\n"
        expected = "1"
        self.assertEqual(run(input_text), expected)

    def test_no_square(self):
        """區間內沒有完全平方數"""
        input_text = "5 8\n0 0\n"
        expected = "0"
        self.assertEqual(run(input_text), expected)


if __name__ == "__main__":
    unittest.main()
