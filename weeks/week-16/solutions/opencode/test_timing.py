"""Stage 1 — @timeit 裝飾器測試

規格: timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫後更新 f.last_elapsed(float 秒)並 append 到 f.records
  4. 裝飾器內不准 print
"""

import time
import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    """@timeit 裝飾器功能驗證"""

    def test_returns_original_result(self):
        """裝飾後函式回傳值與原函式相同"""
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_preserves_function_metadata(self):
        """functools.wraps 保留 __name__ 與 __doc__"""
        @timeit
        def my_function():
            """My docstring"""
            pass

        self.assertEqual(my_function.__name__, "my_function")
        self.assertEqual(my_function.__doc__, "My docstring")

    def test_last_elapsed_and_records_updated(self):
        """呼叫後 last_elapsed 為正 float, records append 該次耗時"""
        @timeit
        def my_function():
            pass

        my_function()
        self.assertIsInstance(my_function.last_elapsed, float)
        self.assertGreater(my_function.last_elapsed, 0)
        self.assertEqual(len(my_function.records), 1)

    def test_decorated_function_with_arguments(self):
        """有參數的函式仍正常執行並回傳正確值"""
        @timeit
        def multiply(x, y):
            return x * y

        result = multiply(6, 7)
        self.assertEqual(result, 42)
        self.assertIsInstance(multiply.last_elapsed, float)

    # ── Edge cases ──

    def test_function_returning_none(self):
        """EDGE: 回傳 None 的函式仍正確記錄耗時"""
        @timeit
        def returns_none():
            return None

        result = returns_none()
        self.assertIsNone(result)
        self.assertIsInstance(returns_none.last_elapsed, float)
        self.assertEqual(len(returns_none.records), 1)

    def test_initial_state_before_any_call(self):
        """EDGE: 尚未呼叫時 records 為空 list, last_elapsed 為 None"""
        @timeit
        def my_function():
            pass

        self.assertEqual(my_function.records, [])
        self.assertIsNone(my_function.last_elapsed)


if __name__ == "__main__":
    unittest.main()
