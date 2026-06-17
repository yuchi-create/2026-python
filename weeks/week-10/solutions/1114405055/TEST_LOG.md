# TEST_LOG

## Task 1 Red

第一次執行測試時，Task 1 測試失敗。

### 錯誤原因

當時 `task1_csv_to_json.py` 中的 `filter_by_admission()` 與 `count_by_dept()` 尚未實作，函式內容仍為 `pass`，因此 Python 預設回傳 `None`。

測試程式原本預期：

- `filter_by_admission()` 應回傳 list
- `count_by_dept()` 應回傳 dict

但實際上函式回傳 `None`，所以造成 `AssertionError` 與 `TypeError`。

### 測試結果摘要

```text
test_count_by_dept_correct ... FAIL
test_count_by_dept_empty ... FAIL
test_count_by_dept_missing_dept_name ... FAIL
test_filter_empty_input ... FAIL
test_filter_keeps_correct_rows ... ERROR
test_filter_missing_admission_key ... ERROR
test_filter_removes_others ... ERROR

FAILED (failures=4, errors=3)
```

---

## Task 1 Green

完成 `filter_by_admission()` 與 `count_by_dept()` 後，重新執行 Task 1 測試，7 個測試全部通過。

### 修正內容

1. `filter_by_admission()` 改為回傳符合指定入學方式的學生資料。
2. 使用 `row.get("入學方式")` 避免資料缺少欄位時發生 `KeyError`。
3. `count_by_dept()` 改為統計每個系所的學生人數。
4. 使用 `row.get("系所名稱")`，缺少系所名稱的資料會被略過。

### 測試結果

```text
test_count_by_dept_correct (test_task1.TestTask1CsvToJson.test_count_by_dept_correct) ... ok
test_count_by_dept_empty (test_task1.TestTask1CsvToJson.test_count_by_dept_empty) ... ok
test_count_by_dept_missing_dept_name (test_task1.TestTask1CsvToJson.test_count_by_dept_missing_dept_name) ... ok
test_filter_empty_input (test_task1.TestTask1CsvToJson.test_filter_empty_input) ... ok
test_filter_keeps_correct_rows (test_task1.TestTask1CsvToJson.test_filter_keeps_correct_rows) ... ok
test_filter_missing_admission_key (test_task1.TestTask1CsvToJson.test_filter_missing_admission_key) ... ok
test_filter_removes_others (test_task1.TestTask1CsvToJson.test_filter_removes_others) ... ok
```

Task 1 測試結果：通過。

---

## Task 2 Red

第一次執行測試時，Task 2 測試失敗。

### 錯誤原因

當時 `task2_json_to_xml.py` 中的 `build_xml_tree()` 尚未實作，函式內容仍為 `pass`，因此回傳 `None`。

測試程式原本預期 `build_xml_tree()` 應該回傳 XML 的 root element，例如：

```xml
<students source="113年新生資料庫" total="2">
```

但實際上回傳 `None`，所以當測試程式呼叫以下屬性或方法時就會失敗：

```python
root.tag
root.findall("student")
root.find("student")
ET.tostring(root, encoding="unicode")
```

### 測試結果摘要

```text
test_empty_student_list ... ERROR
test_missing_student_fields_use_empty_string ... ERROR
test_root_tag_and_attrs ... ERROR
test_student_attrs_exist ... ERROR
test_student_attrs_values_correct ... ERROR
test_student_count_matches ... ERROR
test_xml_is_valid ... ERROR

FAILED (errors=7)
```

---

## Task 2 Green

完成 `build_xml_tree()` 後，重新執行 Task 2 測試，7 個測試全部通過。

### 修正內容

1. 建立 XML 根節點 `<students>`。
2. 在根節點加入 `source` 與 `total` 屬性。
3. 將每一筆學生資料轉成 `<student>` 節點。
4. 每個 `<student>` 節點包含：
   - `id`
   - `dept`
   - `school`
   - `zip`
5. 使用 `student.get()` 避免資料缺少欄位時發生 `KeyError`。
6. 缺少欄位時，預設使用空字串 `""`。

### 測試結果

```text
test_empty_student_list (test_task2.TestTask2JsonToXml.test_empty_student_list) ... ok
test_missing_student_fields_use_empty_string (test_task2.TestTask2JsonToXml.test_missing_student_fields_use_empty_string) ... ok
test_root_tag_and_attrs (test_task2.TestTask2JsonToXml.test_root_tag_and_attrs) ... ok
test_student_attrs_exist (test_task2.TestTask2JsonToXml.test_student_attrs_exist) ... ok
test_student_attrs_values_correct (test_task2.TestTask2JsonToXml.test_student_attrs_values_correct) ... ok
test_student_count_matches (test_task2.TestTask2JsonToXml.test_student_count_matches) ... ok
test_xml_is_valid (test_task2.TestTask2JsonToXml.test_xml_is_valid) ... ok
```

Task 2 測試結果：通過。

---

## Overall Green

完成 Task 1 與 Task 2 修正後，重新執行全部測試：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

整體測試結果：

```text
Ran 14 tests in 0.005s

OK
```

代表 Task 1 與 Task 2 共 14 個測試全部通過。

---

## Refactor 紀錄

完成 Green 階段後，我進行以下整理與重構：

1. 將入學方式篩選邏輯獨立成 `filter_by_admission()`。
2. 將系所人數統計邏輯獨立成 `count_by_dept()`。
3. 將 JSON 輸出資料組裝邏輯獨立成 `build_output_data()`。
4. 將 XML 建立邏輯獨立成 `build_xml_tree()`。
5. 將讀取 CSV、寫入 JSON、讀取 JSON、寫入 XML 分別拆成獨立函式。
6. 使用 `@timeit` 裝飾器記錄主要 I/O 函式執行時間。
7. 寫檔時自動建立 `output/` 資料夾，避免手動建立資料夾造成執行錯誤。
8. 使用 `.get()` 讀取 dictionary 欄位，避免缺少欄位時造成 `KeyError`。
9. 保留測試用的小型假資料，避免 unittest 依賴真實 CSV 檔案。
10. 將 Task 1 與 Task 2 測試分開，讓錯誤來源更容易判斷。

重構後再次執行全部測試，結果仍然通過：

```text
Ran 14 tests in 0.005s

OK
```

---

## 總結

本次 TDD 流程如下：

1. 先建立測試檔案。
2. 執行測試，確認 Task 1 與 Task 2 進入 Red 階段。
3. 依據錯誤訊息補上最小可行功能。
4. 重新測試，確認 Task 1 與 Task 2 進入 Green 階段。
5. 進行 Refactor，整理函式責任與程式結構。
6. 最後重新執行全部測試，確認 14 個測試全部通過。
