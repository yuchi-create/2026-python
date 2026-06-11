"""Stage 4 — plot.py 測試"""

import json
import os
import tempfile
import unittest


class TestLoadResults(unittest.TestCase):
    def test_returns_dict(self):
        from plot import load_results
        data = {"bubble_sort": {"100": 0.01, "200": 0.04}}
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(data, f)
            fname = f.name
        try:
            result = load_results(fname)
            self.assertIsInstance(result, dict)
            self.assertIn("bubble_sort", result)
        finally:
            os.unlink(fname)

    def test_raises_on_missing_file(self):
        from plot import load_results
        with self.assertRaises(FileNotFoundError):
            load_results("/nonexistent/path/results.json")


class TestPlotResults(unittest.TestCase):
    def _make_sample_results(self):
        return {
            "algo_a": {"100": 0.001, "200": 0.004, "400": 0.016},
            "algo_b": {"100": 0.0005, "200": 0.0011, "400": 0.0023},
        }

    def test_png_created_and_nonempty(self):
        from plot import plot_results
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "assets", "test.png")
            plot_results(self._make_sample_results(), out_path)
            self.assertTrue(os.path.exists(out_path), "PNG 檔案未生成")
            self.assertGreater(os.path.getsize(out_path), 0, "PNG 是空檔")

    def test_png_is_valid_png_header(self):
        """驗證輸出確實是 PNG 格式（magic bytes）"""
        from plot import plot_results
        with tempfile.TemporaryDirectory() as tmpdir:
            out_path = os.path.join(tmpdir, "assets", "check.png")
            plot_results(self._make_sample_results(), out_path)
            with open(out_path, "rb") as f:
                header = f.read(8)
            self.assertEqual(header[:4], b"\x89PNG", "輸出不是合法 PNG")

    def test_output_dir_autocreated(self):
        """out_path 的父目錄若不存在，應自動建立"""
        from plot import plot_results
        with tempfile.TemporaryDirectory() as tmpdir:
            nested = os.path.join(tmpdir, "deep", "nested", "dir", "out.png")
            plot_results(self._make_sample_results(), nested)
            self.assertTrue(os.path.exists(nested))


if __name__ == "__main__":
    unittest.main()
