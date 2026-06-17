# Week 10 Homework：CSV / JSON / XML 資料格式轉換

## 專案說明

本專案為 Week 10 回家作業，主題是資料格式轉換與執行時間比較。主要目標是使用 Python 讀取真實 CSV 資料，完成資料篩選、統計、JSON 輸出、XML 轉換，並透過 `@timeit` 裝飾器記錄函式執行時間，最後使用 `matplotlib` 產生效能比較圖。

本次作業依照 TDD 流程完成 Task 1 與 Task 2，流程包含：

```text
Red → Green → Refactor
```

---

## 完成項目

- [x] Task 1：讀取 CSV，篩選 `入學方式 == 聯合登記分發`
- [x] Task 1：統計篩選後學生的各系所人數
- [x] Task 1：輸出 `output/students.json`
- [x] Task 2：讀取 `students.json`
- [x] Task 2：將學生清單轉換成 XML
- [x] Task 2：輸出 `output/students.xml`
- [x] Task 3：讀取 `TIMING_REPORT.md` 中的 timeit 結果
- [x] Task 3：使用 `matplotlib` 產生 `output/timing_comparison.png`
- [x] 使用 `unittest` 完成 Task 1 / Task 2 測試
- [x] 完成 `TEST_LOG.md`
- [x] 完成 `TIMING_REPORT.md`
- [x] 完成 `AI_USAGE.md`

---

## 專案架構

```text
weeks/week-10/solutions/1114405055/
├── task1_csv_to_json.py
├── task2_json_to_xml.py
├── task3_plot_comparison.py
├── output/
│   ├── students.json
│   ├── students.xml
│   └── timing_comparison.png
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
├── README.md
├── TEST_LOG.md
├── TIMING_REPORT.md
├── AI_USAGE.md
└── ToDo.md
```

---

## 環境需求

本作業主要使用 Python 內建模組：

```text
csv
json
os
time
functools
xml.etree.ElementTree
unittest
re
pathlib
```

Task 3 需要額外安裝：

```text
matplotlib
```

安裝方式：

```powershell
python -m pip install matplotlib
```

確認是否安裝成功：

```powershell
python -c "import matplotlib; print(matplotlib.__version__)"
```

---

## 執行方式

請先進入作業資料夾：

```powershell
cd weeks/week-10/solutions/1114405055
```

---

### 1. 執行測試

執行全部測試：

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

本次測試結果：

```text
Ran 14 tests in 0.005s

OK
```

Task 1 測試數量：7 個  
Task 2 測試數量：7 個  
合計：14 個測試

---

### 2. 執行 Task 1：CSV 轉 JSON

```powershell
python task1_csv_to_json.py
```

成功後會產生：

```text
output/students.json
```

終端機會顯示類似：

```text
[timeit] read_csv 耗時 0.003385s
[timeit] write_json 耗時 0.005483s
JSON 已儲存：output/students.json
```

---

### 3. 執行 Task 2：JSON 轉 XML

```powershell
python task2_json_to_xml.py
```

成功後會產生：

```text
output/students.xml
```

終端機會顯示類似：

```text
[timeit] read_json 耗時 0.001577s
[timeit] write_xml 耗時 0.003819s
XML 已儲存：output/students.xml
```

---

### 4. 執行 Task 3：產生效能比較圖

```powershell
python task3_plot_comparison.py
```

成功後會產生：

```text
output/timing_comparison.png
```

終端機會顯示：

```text
圖表已儲存：output/timing_comparison.png
```

---

## timeit 裝飾器說明

本專案在 Task 1 與 Task 2 中自行實作 `@timeit` 裝飾器，用來記錄函式執行時間。

裝飾器邏輯如下：

1. 在目標函式執行前使用 `time.perf_counter()` 記錄開始時間。
2. 執行原本的函式。
3. 函式完成後再次使用 `time.perf_counter()` 記錄結束時間。
4. 計算結束時間與開始時間的差值。
5. 印出函式名稱與耗時秒數。
6. 回傳原本函式的執行結果。

本次套用 `@timeit` 的函式包含：

```text
task1_csv_to_json.py
- read_csv()
- write_json()

task2_json_to_xml.py
- read_json()
- write_xml()
```

---

## TDD 測試說明

本作業依照 TDD 流程完成：

```text
Red → Green → Refactor
```

### Red

一開始先撰寫測試，但核心函式尚未完成，因此測試失敗。例如：

- `filter_by_admission()` 尚未實作，回傳 `None`
- `count_by_dept()` 尚未實作，回傳 `None`
- `build_xml_tree()` 尚未實作，回傳 `None`

因此測試出現：

```text
TypeError: object of type 'NoneType' has no len()
AttributeError: 'NoneType' object has no attribute 'findall'
AssertionError: None != {}
```

### Green

補上最小可行功能後，測試通過：

- `filter_by_admission()` 回傳符合指定入學方式的學生資料
- `count_by_dept()` 回傳各系所統計結果
- `build_xml_tree()` 回傳 XML root element

### Refactor

測試通過後，整理程式結構：

- 將 CSV 讀取、篩選、統計、輸出 JSON 拆成獨立函式
- 將 JSON 讀取、XML 建立、XML 輸出拆成獨立函式
- 寫檔時自動建立 `output/` 資料夾
- 使用 `.get()` 避免缺少欄位時發生 `KeyError`
- 保留測試用假資料，避免單元測試依賴真實 CSV

---

## 測試涵蓋範圍

### Task 1 測試

```text
test_filter_keeps_correct_rows
test_filter_removes_others
test_filter_empty_input
test_filter_missing_admission_key
test_count_by_dept_correct
test_count_by_dept_empty
test_count_by_dept_missing_dept_name
```

涵蓋內容：

- 正常篩選
- 排除其他入學方式
- 空輸入
- 缺少欄位
- 系所統計
- 空統計

---

### Task 2 測試

```text
test_root_tag_and_attrs
test_student_count_matches
test_student_attrs_exist
test_student_attrs_values_correct
test_empty_student_list
test_xml_is_valid
test_missing_student_fields_use_empty_string
```

涵蓋內容：

- XML 根節點
- XML root attributes
- student 節點數量
- student attributes
- 空學生清單
- XML 是否可被正常解析
- 缺少欄位時是否使用空字串

---

## timeit 執行結果摘要

本次實測結果如下：

```text
[timeit] read_csv 耗時 0.003385s
[timeit] write_json 耗時 0.005483s
[timeit] read_json 耗時 0.001577s
[timeit] write_xml 耗時 0.003819s
```

觀察結果：

- `write_json` 為本次最耗時的操作。
- `read_csv` 比 `read_json` 慢。
- 本次 `write_xml` 比 `write_json` 快。
- 若資料筆數增加，讀取與寫入時間都會增加，寫入類操作可能受格式化與檔案大小影響更明顯。

詳細分析請見：

```text
TIMING_REPORT.md
```

---

## 遇到的問題與修正

### 問題 1：函式尚未實作造成 NoneType 錯誤

第一次執行測試時，因為核心函式仍為 `pass`，所以回傳 `None`，導致測試失敗。

修正方式：

- 補上 `filter_by_admission()`
- 補上 `count_by_dept()`
- 補上 `build_xml_tree()`

修正後，14 個測試全部通過。

---

### 問題 2：CSV 路徑錯誤造成 FileNotFoundError

執行 Task 1 時曾出現：

```text
FileNotFoundError: [Errno 2] No such file or directory
```

原因是程式中的 CSV 相對路徑與實際檔案位置不一致。

修正方式：

- 檢查資料檔實際位置
- 將 `DEFAULT_CSV_PATH` 改成能讀到資料檔的路徑
- 理解相對路徑與執行位置的關係

---

## 輸出檔案

本作業會產生以下輸出：

```text
output/students.json
output/students.xml
output/timing_comparison.png
```

其中：

- `students.json`：CSV 篩選與統計後的 JSON 結果
- `students.xml`：由 JSON 轉換而成的 XML 結果
- `timing_comparison.png`：四個核心 I/O 函式的耗時比較圖

---

## 最終確認

本專案目前已完成：

```text
Task 1：完成
Task 2：完成
Task 3：完成
unittest：14 tests OK
TEST_LOG：完成
TIMING_REPORT：完成
AI_USAGE：完成
README：完成
```
