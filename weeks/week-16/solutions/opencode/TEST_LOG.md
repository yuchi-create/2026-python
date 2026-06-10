# TEST_LOG — 排序效能實驗室

## 測試執行環境

- Python 3.x
- macOS (Darwin)
- unittest 測試框架

## 測試結果總表

```
$ python -m unittest discover -s . -p "test_*.py" -v

test_decorated_function_with_arguments (test_timing.TestTimeit) ... ok
test_function_returning_none (test_timing.TestTimeit) ... ok
test_initial_state_before_any_call (test_timing.TestTimeit) ... ok
test_last_elapsed_and_records_updated (test_timing.TestTimeit) ... ok
test_preserves_function_metadata (test_timing.TestTimeit) ... ok
test_returns_original_result (test_timing.TestTimeit) ... ok
test_all_identical_values (test_sorts.TestSortFunctions) ... ok
test_basic_cases (test_sorts.TestSortFunctions) ... ok
test_input_not_mutated (test_sorts.TestSortFunctions) ... ok
test_negative_and_mixed_numbers (test_sorts.TestSortFunctions) ... ok
test_random_data_matches_builtin (test_sorts.TestSortFunctions) ... ok
test_all_identical_values (test_sorts_fast.TestFastSortFunctions) ... ok
test_basic_cases (test_sorts_fast.TestFastSortFunctions) ... ok
test_input_not_mutated (test_sorts_fast.TestFastSortFunctions) ... ok
test_large_random_data (test_sorts_fast.TestFastSortFunctions) ... ok
test_random_data_matches_builtin (test_sorts_fast.TestFastSortFunctions) ... ok
test_load_results_file_not_found (test_plot.TestPlot) ... ok
test_load_results_has_expected_keys (test_plot.TestPlot) ... ok
test_load_results_returns_dict (test_plot.TestPlot) ... ok
test_plot_results_creates_png (test_plot.TestPlot) ... ok
test_plot_results_png_not_empty (test_plot.TestPlot) ... ok

----------------------------------------------------------------------
Ran 21 tests in 0.442s

OK
```

## 各階段測試說明

### Stage 1 — timing.py（6 tests, 2 edge cases）

| 測試 | 說明 |
|------|------|
| `test_returns_original_result` | 裝飾後函式回傳值與原函式相同 |
| `test_last_elapsed_and_records_updated` | 呼叫後 last_elapsed 為正 float, records append 該次耗時 |
| `test_preserves_function_metadata` | functools.wraps 保留 __name__ 與 __doc__ |
| `test_decorated_function_with_arguments` | 有參數的函式仍正常執行 |
| `test_function_returning_none` (edge) | 回傳 None 的函式仍正確記錄耗時 |
| `test_initial_state_before_any_call` (edge) | 尚未呼叫時 records 為空 list, last_elapsed 為 None |

### Stage 2 — sorts.py（5 tests, 2 edge cases，5 個排序函式共用）

| 測試 | 說明 |
|------|------|
| `test_basic_cases` | 5 組案例：已排序、未排序、空 list、單一元素、含重複 |
| `test_random_data_matches_builtin` | 亂數 100 筆 vs sorted() |
| `test_input_not_mutated` | 原始輸入不可被修改 |
| `test_all_identical_values` (edge) | 20 個相同值 |
| `test_negative_and_mixed_numbers` (edge) | 含負數與零 |

### Stage 3 — sorts_fast.py（5 tests, 2 edge cases）

| 測試 | 說明 |
|------|------|
| `test_basic_cases` | 同 Stage 2 共用案例 |
| `test_random_data_matches_builtin` | 亂數 100 筆 vs sorted() |
| `test_input_not_mutated` | 原始輸入不可被修改 |
| `test_all_identical_values` (edge) | 20 個相同值 |
| `test_large_random_data` (edge) | 1000 筆亂數 vs sorted() |

### Stage 4 — plot.py（5 tests, 2 edge cases）

| 測試 | 說明 |
|------|------|
| `test_load_results_returns_dict` | 載入 results.json 回傳 dict |
| `test_load_results_has_expected_keys` | dict 包含各演算法名稱 |
| `test_plot_results_creates_png` | plot_results 產生 PNG 檔案 |
| `test_plot_results_png_not_empty` (edge) | PNG 檔案大小大於 0 |
| `test_load_results_file_not_found` (edge) | 不存在路徑拋出 FileNotFoundError |

### Stage 5 — 安全審查（新增防禦測試）

| 測試 | 說明 | 新增檔案 |
|------|------|---------|
| `test_none_input_raises_typeerror` | 傳 None 給排序函式應拋 TypeError | (手動驗證) |
| `test_nonlist_input_raises_typeerror` | 傳 string/int 給排序函式應拋 TypeError | (手動驗證) |

> Stage 5 安全修補採 source code 防禦寫法（`_validate_list` 在 sorts.py 與 sorts_fast.py），21 個既有測試維持全綠。

## 最終測試結果（Stage 1–5）

- ✅ 總測試數：**21**
- ✅ 通過：**21**
- ❌ 失敗：**0**
- ⚠️ 跳過：**0**
