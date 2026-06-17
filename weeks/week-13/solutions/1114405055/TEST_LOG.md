# TEST_LOG.md — TDD Red → Green 執行紀錄

## Red Phase（測試先行，尚未實作）

執行時間：2026-06-17

```
python -m unittest discover -s tests -v

test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ERROR
test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ERROR
test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ERROR
test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ERROR
test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ERROR
test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ERROR
test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ERROR
test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ERROR
test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ERROR
test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ERROR

----------------------------------------------------------------------
Ran 10 tests in 0.004s

FAILED (errors=10)
```

**失敗原因：** `task1_grouped_bar` 與 `task2_zipcode_heatmap` 模組尚未建立，所有測試在 `setUp` 即拋出 `ModuleNotFoundError`。

---

## Green Phase（實作完成後）

執行時間：2026-06-17

```
python -m unittest discover -s tests -v

test_get_top_depts_includes_popular (test_task1.TestTask1.test_get_top_depts_includes_popular) ... ok
test_get_top_depts_length (test_task1.TestTask1.test_get_top_depts_length) ... ok
test_load_year_counts_correct (test_task1.TestTask1.test_load_year_counts_correct) ... ok
test_load_year_returns_dict (test_task1.TestTask1.test_load_year_returns_dict) ... ok
test_load_year_total_positive (test_task1.TestTask1.test_load_year_total_positive) ... ok
test_get_top_counties_length (test_task2.TestTask2.test_get_top_counties_length) ... ok
test_load_county_counts_penghu_positive (test_task2.TestTask2.test_load_county_counts_penghu_positive) ... ok
test_load_county_counts_type (test_task2.TestTask2.test_load_county_counts_type) ... ok
test_zip_to_county_penghu (test_task2.TestTask2.test_zip_to_county_penghu) ... ok
test_zip_to_county_unknown (test_task2.TestTask2.test_zip_to_county_unknown) ... ok

----------------------------------------------------------------------
Ran 10 tests in 1.116s

OK
```

**10/10 通過。**

### 實作過程摘要

1. 依作業規格實作 `load_year` / `get_top_depts`（Task 1）與 `zip_to_county` / `load_county_counts` / `get_top_counties`（Task 2）。
2. `DATA_DIR` 採用 `Path(__file__).parent.parent.parent.parent.parent`（共 5 層）由解題目錄回到專案根目錄，再接上 `assets/stu-data`，測試檔則多一層（6 層）回到根目錄。
3. `get_top_depts` 先取各年前 top_n 名系所的聯集，再依六年（三年）合計人數排序後截取前 top_n 項，確保回傳數量不超過 `top_n`。
4. `zip_to_county` 對郵遞區號前 3 碼建立對照表，並修正了講義範例中 950–953 區段重複出現於屏東縣與台東縣的問題（950–953 實際對應台東縣）。
