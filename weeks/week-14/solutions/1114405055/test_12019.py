# test_12019.py - UVA 12019 測試程式
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "12019.py"


def run(input_text):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


class TestDoomsDay(unittest.TestCase):
    def test_doomsday_dates_are_wednesday(self):
        """每個月的 Doomsday 日期本身都應該是星期三"""
        input_text = (
            "12\n"
            "1 10\n2 21\n3 7\n4 4\n5 9\n6 6\n"
            "7 11\n8 8\n9 5\n10 10\n11 7\n12 12\n"
        )
        expected = "\n".join(["Wednesday"] * 12)
        self.assertEqual(run(input_text), expected)

    def test_other_dates(self):
        """非 Doomsday 日期的星期推算"""
        input_text = "2\n1 1\n1 11\n"
        expected = "Monday\nThursday"
        self.assertEqual(run(input_text), expected)


if __name__ == "__main__":
    unittest.main()
