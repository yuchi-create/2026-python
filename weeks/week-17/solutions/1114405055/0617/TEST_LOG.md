# TEST_LOG — 0617

## 任務一 `timing.py`(完整 TDD)

### 紅燈(timing.py 尚未存在)

```
$ python -m unittest test_timing -v
ImportError: Failed to import test module: test_timing
ModuleNotFoundError: No module named 'timing'

Ran 1 test in 0.000s

FAILED (errors=1)
```

### 綠燈(寫完 timing.py 之後)

```
$ python -m unittest test_timing -v
test_exception_propagates_and_not_recorded ... ok
test_preserves_function_metadata ... ok
test_records_accumulates_across_calls ... ok
test_rejects_invalid_repeat ... ok
test_repeat_runs_n_times ... ok
test_returns_value_unchanged ... ok

Ran 6 tests in 0.000s

OK
```

## 任務二 `search.py`(輕量,不要求完整紅綠燈)

```
$ python -m unittest test_search -v
test_does_not_mutate_input (TestBinarySearch) ... ok
test_found_sorted (TestBinarySearch) ... ok
test_not_found_sorted (TestBinarySearch) ... ok
test_does_not_mutate_input (TestLinearSearch) ... ok
test_found (TestLinearSearch) ... ok
test_not_found (TestLinearSearch) ... ok

Ran 6 tests in 0.000s

OK
```

## 效能評估 `benchmark.py`

```
$ python benchmark.py
n = 200000, target = 最後一個元素(最壞情況)
linear_search  records = [0.0060637..., 0.0053461..., 0.0054251..., 0.0053499..., 0.0054170...]
linear_search  last_elapsed (avg of 5 runs) = 0.005520 s
binary_search  records = [4.3e-06, 2.4e-06, 1.7e-06, 1.5e-06, 1.6e-06]
binary_search  last_elapsed (avg of 5 runs) = 0.000002 s
linear / binary 倍數 = 2400.2x
```
