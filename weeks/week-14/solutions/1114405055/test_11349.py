# test_11349.py - UVA 11349 測試程式
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "11349.py"


def run(input_text):
    """執行手打程式並回傳標準輸出"""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class TestSymmetricMatrix(unittest.TestCase):
    def test_sample(self):
        """題目給的範例測資"""
        input_text = (
            "2\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "3 1 5\n"
            "N = 3\n"
            "5 1 3\n"
            "2 0 2\n"
            "0 1 5\n"
        )
        expected = "Test #1: Symmetric.\nTest #2: Non-symmetric."
        self.assertEqual(run(input_text), expected)

    def test_negative_value(self):
        """含有負數的矩陣，必為 Non-symmetric"""
        input_text = "1\nN = 2\n1 2\n2 -1\n"
        expected = "Test #1: Non-symmetric."
        self.assertEqual(run(input_text), expected)

    def test_single_element(self):
        """1x1 矩陣，只要非負一定是 Symmetric"""
        input_text = "1\nN = 1\n7\n"
        expected = "Test #1: Symmetric."
        self.assertEqual(run(input_text), expected)


if __name__ == "__main__":
    unittest.main()
