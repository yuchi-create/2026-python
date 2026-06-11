"""Stage 1 — @timeit 裝飾器測試"""

import io
import sys
import time
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        """被裝飾函式的回傳值必須不變"""
        @timeit
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_preserves_function_metadata(self):
        """functools.wraps 必須保留 __name__ 與 __doc__"""
        @timeit
        def my_func():
            """My docstring"""

        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "My docstring")

    def test_records_elapsed_time(self):
        """每次呼叫後 last_elapsed 應為正數 float，records 應累積"""
        @timeit
        def slow():
            time.sleep(0.01)

        slow()
        self.assertIsInstance(slow.last_elapsed, float)
        self.assertGreater(slow.last_elapsed, 0)
        self.assertEqual(len(slow.records), 1)
        self.assertAlmostEqual(slow.last_elapsed, slow.records[0])

    def test_records_accumulate_across_calls(self):
        """多次呼叫後 records 長度應等於呼叫次數，last_elapsed 等於最後一筆"""
        @timeit
        def noop():
            pass

        for _ in range(5):
            noop()

        self.assertEqual(len(noop.records), 5)
        self.assertEqual(noop.last_elapsed, noop.records[-1])

    def test_no_print_side_effect(self):
        """裝飾器本身不能有任何 print 輸出"""
        @timeit
        def silent():
            return 42

        captured = io.StringIO()
        sys.stdout = captured
        try:
            result = silent()
        finally:
            sys.stdout = sys.__stdout__

        self.assertEqual(result, 42)
        self.assertEqual(captured.getvalue(), "")

    def test_independent_instances(self):
        """不同被裝飾函式的 records 互相獨立"""
        @timeit
        def f1():
            pass

        @timeit
        def f2():
            pass

        f1()
        f1()
        f2()

        self.assertEqual(len(f1.records), 2)
        self.assertEqual(len(f2.records), 1)


if __name__ == "__main__":
    unittest.main()
