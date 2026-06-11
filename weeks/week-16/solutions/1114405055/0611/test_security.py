"""Stage 5 — 安全性自掃測試

對照 OpenSSF Secure Coding Guide for Python 四個章節：
  08 Coding Standards / 05 Exception Handling / 03 Numbers / 04 Neutralization

每條先讓測試紅燈，修正後轉綠。
"""

import json
import os
import sys
import tempfile
import unittest


# ── 08 Coding Standards ─────────────────────────────────────────────────────

class TestFileHandlingWithContext(unittest.TestCase):
    """08: 開檔讀寫必須用 with 語法確保關檔"""

    def test_results_json_written_with_context(self):
        """benchmark.py 寫 results.json 應用 with open，確保檔案正確關閉"""
        import inspect
        import benchmark
        src = inspect.getsource(benchmark)
        # 確認寫 json 是在 with 區塊內（出現 with open ... "w" ...）
        self.assertIn("with open", src,
                      "benchmark.py 未使用 with open 寫檔，檔案可能未關閉")

    def test_plot_load_uses_context(self):
        """plot.load_results 讀檔應用 with open"""
        import inspect
        import plot
        src = inspect.getsource(plot.load_results)
        self.assertIn("with open", src,
                      "load_results 未使用 with open，檔案可能未關閉")


# ── 04 Neutralization / CWE-502 ─────────────────────────────────────────────

class TestNoPickle(unittest.TestCase):
    """04: 讀寫 results.json 應用 json，不得用 pickle（CWE-502）"""

    def test_benchmark_does_not_import_pickle(self):
        import benchmark
        self.assertNotIn("pickle", dir(benchmark),
                         "benchmark.py 不應 import pickle")

    def test_plot_uses_json_not_pickle(self):
        """load_results 必須用 json.load，不得呼叫 pickle.load"""
        import inspect
        import plot
        src = inspect.getsource(plot.load_results)
        self.assertIn("json.load", src,
                      "load_results 應使用 json.load 而非 pickle")
        # 僅禁止呼叫 pickle.load，docstring 中提及 pickle 是說明原因，不算違規
        self.assertNotIn("pickle.load", src,
                         "load_results 不應呼叫 pickle.load（CWE-502）")


# ── 05 Exception Handling ───────────────────────────────────────────────────

class TestSpecificExceptions(unittest.TestCase):
    """05: 應捕捉具體例外，不得用裸 except:"""

    def test_no_bare_except_in_plot(self):
        import inspect
        import plot
        src = inspect.getsource(plot)
        self.assertNotIn("except:", src,
                         "plot.py 有裸 except:，應指定具體例外類型")

    def test_no_bare_except_in_benchmark(self):
        import inspect
        import benchmark
        src = inspect.getsource(benchmark)
        self.assertNotIn("except:", src,
                         "benchmark.py 有裸 except:，應指定具體例外類型")

    def test_load_results_raises_file_not_found(self):
        """load_results 在檔案不存在時應傳播 FileNotFoundError"""
        from plot import load_results
        with self.assertRaises(FileNotFoundError):
            load_results("/no/such/file.json")


# ── 03 Numbers ──────────────────────────────────────────────────────────────

class TestInputValidation(unittest.TestCase):
    """03: make_data 的 n 應驗證邊界，負數應 raise ValueError"""

    def test_make_data_rejects_negative_n(self):
        from benchmark import make_data
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_accepts_zero(self):
        from benchmark import make_data
        self.assertEqual(make_data(0), [])

    def test_make_data_accepts_positive(self):
        from benchmark import make_data
        data = make_data(10)
        self.assertEqual(len(data), 10)


# ── 08 Coding Standards — shadow 內建名稱 ───────────────────────────────────

class TestNoShadowBuiltins(unittest.TestCase):
    """08: 不得用 list / sorted 等內建名稱當變數名"""

    def test_sorts_does_not_shadow_list(self):
        import inspect
        import sorts
        src = inspect.getsource(sorts)
        # 簡單掃描：不應出現 "list = " 或 "sorted = " 這樣的賦值
        self.assertNotIn("list = ", src,
                         "sorts.py shadow 了內建 list")
        self.assertNotIn("sorted = ", src,
                         "sorts.py shadow 了內建 sorted")


if __name__ == "__main__":
    unittest.main()
