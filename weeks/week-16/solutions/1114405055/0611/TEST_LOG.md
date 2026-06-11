# TEST_LOG — Week 16 排序效能實驗室（0611）

每階段紅燈 → 綠燈的 `python -m unittest` 輸出。

---

## Stage 1 — `@timeit` 裝飾器

### 紅燈（timing.py 尚未建立）

```
EEEEEE
======================================================================
ERROR: test_independent_instances (test_timing.TestTimeit...)
ModuleNotFoundError: No module named 'timing'
...（共 6 個 ERROR）

Ran 6 tests in 0.004s
FAILED (errors=6)
```

### 綠燈（timing.py 完成後）

```
test_independent_instances ... ok
test_no_print_side_effect ... ok
test_preserves_function_metadata ... ok
test_records_accumulate_across_calls ... ok
test_records_elapsed_time ... ok
test_returns_original_result ... ok

Ran 6 tests in 0.068s
OK
```

---

## Stage 2 — 三種排序 + benchmark

### 紅燈（sorts.py 尚未建立）

```
EEEEEEEEE
ERROR: test_all_same_elements (test_sorts.TestSortFunctions...)
ModuleNotFoundError: No module named 'sorts'
...（共 9 個 ERROR）

Ran 9 tests in 0.003s
FAILED (errors=9)
```

### 綠燈（sorts.py + benchmark.py 完成後）

```
test_all_same_elements ... ok
test_already_sorted ... ok
test_basic_cases ... ok
test_duplicates ... ok
test_empty_list ... ok
test_input_not_mutated ... ok
test_random_data_matches_builtin ... ok
test_reverse_sorted ... ok
test_single_element_list ... ok

Ran 9 tests in 0.016s
OK
```

---

## Stage 3 — 加速版（quick_sort_med3）

`quick_sort_med3` append 進 `SORT_FUNCTIONS` 後，Stage 2 同一組測試全數通過：

```
test_all_same_elements ... ok  (含 med3)
test_already_sorted ... ok
test_basic_cases ... ok
test_duplicates ... ok
test_empty_list ... ok
test_input_not_mutated ... ok  (med3 也不改輸入)
test_random_data_matches_builtin ... ok
test_reverse_sorted ... ok
test_single_element_list ... ok

Ran 9 tests in 0.021s
OK
```

---

## Stage 4 — 畫圖

### 紅燈（plot.py 尚未建立）

```
EEEE
ERROR: test_load_results_raises_file_not_found ...
ModuleNotFoundError: No module named 'plot'
...

Ran 4 tests in 0.002s
FAILED (errors=4)
```

### 綠燈（plot.py 完成後）

```
test_load_results_raises_file_not_found ... ok
test_output_dir_autocreated ... ok
test_png_created_and_nonempty ... ok
test_png_is_valid_png_header ... ok
test_returns_dict ... ok

Ran 5 tests in 0.724s
OK
```

---

## Stage 5 — 安全自掃

### 紅燈（test_security.py 中 pickle 測試誤判，修正前）

```
FAIL: test_plot_uses_json_not_pickle ...
AssertionError: 'pickle' unexpectedly found in source...

Ran 31 tests in 0.629s
FAILED (failures=1)
```

問題：`assertNotIn("pickle", src)` 把 docstring 中說明原因的文字也掃到了。
修正：改為 `assertNotIn("pickle.load", src)` 只禁止呼叫，不禁止提及。

### 綠燈（修正後）

```
test_benchmark_does_not_import_pickle ... ok
test_load_results_raises_file_not_found ... ok
test_make_data_accepts_positive ... ok
test_make_data_accepts_zero ... ok
test_make_data_rejects_negative_n ... ok
test_no_bare_except_in_benchmark ... ok
test_no_bare_except_in_plot ... ok
test_plot_load_uses_context ... ok
test_plot_uses_json_not_pickle ... ok
test_results_json_written_with_context ... ok
test_sorts_does_not_shadow_list ... ok

Ran 11 tests in 0.041s
OK
```

---

## 全部測試彙總（所有 Stage）

```
Ran 31 tests in 0.634s
OK
```
