"""0617 任務一 — timeit 裝飾器測試

規格:timing.py 的 timeit 裝飾器必須
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)
  6. repeat 必須是 int(非 bool 以外的型別一律拒絕),否則 raise ValueError
  7. 被裝飾函式內部拋例外時,例外原樣往外傳,且該輪不計入 records

提醒:
  - test_rejects_invalid_repeat 就是本日的安全測試(raise 而非 assert)。
  - edge case:repeat=1、副作用函式是否被多算、例外是否被吞掉。
"""

import unittest

from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_value_unchanged(self):
        @timeit()
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_preserves_function_metadata(self):
        @timeit()
        def add(a, b):
            """加總兩個數"""
            return a + b

        self.assertEqual(add.__name__, "add")
        self.assertEqual(add.__doc__, "加總兩個數")

    def test_repeat_runs_n_times(self):
        counter = {"calls": 0}

        @timeit(repeat=5)
        def side_effect():
            counter["calls"] += 1
            return counter["calls"]

        side_effect()
        self.assertEqual(counter["calls"], 5)

    def test_records_accumulates_across_calls(self):
        @timeit(repeat=3)
        def noop():
            return None

        noop()
        noop()
        self.assertEqual(len(noop.records), 6)
        self.assertTrue(all(isinstance(t, float) for t in noop.records))
        self.assertIsInstance(noop.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            timeit(repeat=0)

        with self.assertRaises(ValueError):
            timeit(repeat=-1)

        with self.assertRaises(ValueError):
            timeit(repeat="3")

        with self.assertRaises(ValueError):
            timeit(repeat=2.5)

    def test_exception_propagates_and_not_recorded(self):
        @timeit(repeat=3)
        def boom():
            raise RuntimeError("kaboom")

        with self.assertRaises(RuntimeError):
            boom()
        self.assertEqual(len(boom.records), 0)


if __name__ == "__main__":
    unittest.main()
