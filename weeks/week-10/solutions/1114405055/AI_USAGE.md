# AI_USAGE

## 我問了 AI 哪些問題？

1. 如何針對 Week 10 Homework 建立專案架構？
2. 如何撰寫 Task 1 與 Task 2 的 unittest 測試程式？
3. 如何執行 `python -m unittest discover -s tests -p "test_*.py" -v`？
4. 當測試出現 `NoneType`、`AttributeError`、`AssertionError` 時，如何判斷錯誤原因？
5. 如何修正 `filter_by_admission()`、`count_by_dept()` 與 `build_xml_tree()`？
6. 如何執行 Task 1、Task 2 並產出 `students.json` 與 `students.xml`？
7. 當執行 `task1_csv_to_json.py` 出現 `FileNotFoundError` 時，如何修正 CSV 路徑問題？

---

## 我採用的 AI 建議

### 1. 採用 TDD 開發流程

我採用 AI 建議，先建立測試檔：

```text
tests/test_task1.py
tests/test_task2.py
```

並先執行測試確認 Red 階段，再逐步修正程式讓測試進入 Green 階段。

---

### 2. 採用單元測試拆分 Task 1 與 Task 2

我採用 AI 建議，將測試分為：

```text
Task 1：CSV 過濾與系所統計測試
Task 2：JSON 轉 XML 結構測試
```

Task 1 測試內容包含：

```text
filter_by_admission()
count_by_dept()
空輸入
缺少欄位
排除非指定入學方式
```

Task 2 測試內容包含：

```text
XML root tag
root attributes
student 數量
student attributes
空學生清單
XML 是否可被正常解析
缺少欄位時是否使用空字串
```

---

### 3. 採用 `row.get()` 避免缺少欄位造成錯誤

在 Task 1 中，我採用 AI 建議使用：

```python
row.get("入學方式")
row.get("系所名稱")
```

避免資料中缺少指定欄位時直接造成 `KeyError`。

---

### 4. 採用 `ET.Element` 與 `ET.SubElement` 建立 XML

在 Task 2 中，我採用 AI 建議使用 Python 內建的：

```python
xml.etree.ElementTree
```

建立 XML 結構，而不是手動用字串拼接 XML，這樣可以降低 XML 格式錯誤的風險。

---

### 5. 採用 `pathlib` 作為後續修正方向

這次執行 Task 1 時發生 CSV 路徑錯誤，因此後續建議採用：

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CSV_PATH = BASE_DIR.parent.parent / "113年新生資料庫.csv"
DEFAULT_OUTPUT_PATH = BASE_DIR / "output" / "students.json"
```

這樣可以避免因為目前終端機所在位置不同，而導致相對路徑失效。

---

## 我拒絕的 AI 建議

### 1. 沒有採用手動建立 `output/` 資料夾

AI 曾建議可以手動檢查或建立 `output/`，但我決定讓程式自動建立：

```python
os.makedirs(directory, exist_ok=True)
```

原因是 `output/` 屬於程式產生的輸出資料夾，讓程式自動建立比較符合自動化流程。

---

### 2. 沒有把所有函式都加上 `@timeit`

我只保留作業要求的主要 I/O 函式加上 `@timeit`，例如：

```text
read_csv()
write_json()
read_json()
write_xml()
```

沒有把 `filter_by_admission()`、`count_by_dept()`、`build_xml_tree()` 全部加上 `@timeit`。

原因是這樣可以避免終端機輸出過於混亂，也比較符合作業要求。

---

## AI 輸出錯誤與修正案例

### 錯誤案例 1：第一次測試失敗，函式回傳 None

#### 錯誤現象

第一次執行測試時，出現以下錯誤：

```text
TypeError: object of type 'NoneType' has no len()
AttributeError: 'NoneType' object has no attribute 'findall'
AssertionError: None != {}
```

#### 錯誤原因

原因是 `task1_csv_to_json.py` 與 `task2_json_to_xml.py` 中的核心函式仍然是 `pass`，例如：

```python
def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    pass

def count_by_dept(rows: list[dict]) -> dict:
    pass

def build_xml_tree(data: dict) -> ET.Element:
    pass
```

Python 函式如果只有 `pass`，沒有 `return`，預設會回傳 `None`，所以測試程式在呼叫 `len(result)`、`root.findall()`、`root.tag` 時就會失敗。

#### 修正方式

我補上實作：

```python
def filter_by_admission(rows: list[dict], method: str) -> list[dict]:
    return [
        row
        for row in rows
        if row.get("入學方式") == method
    ]
```

```python
def count_by_dept(rows: list[dict]) -> dict:
    dept_count = {}

    for row in rows:
        dept = row.get("系所名稱")

        if not dept:
            continue

        dept_count[dept] = dept_count.get(dept, 0) + 1

    return dept_count
```

```python
def build_xml_tree(data: dict) -> ET.Element:
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(data.get("總人數", 0)),
        },
    )

    students = data.get("學生清單", [])

    for student in students:
        ET.SubElement(
            root,
            "student",
            {
                "id": str(student.get("學號", "")),
                "dept": str(student.get("系所名稱", "")),
                "school": str(student.get("畢業學校", "")),
                "zip": str(student.get("郵遞區號", "")),
            },
        )

    return root
```

#### 修正後結果

重新執行測試後，14 個測試全部通過：

```text
Ran 14 tests in 0.005s

OK
```

---

### 錯誤案例 2：執行 Task 1 時找不到 CSV 檔案

#### 錯誤現象

執行：

```powershell
python task1_csv_to_json.py
```

出現錯誤：

```text
FileNotFoundError: [Errno 2] No such file or directory: '../../113年新生資料庫.csv'
```

完整錯誤位置顯示：

```text
File "task1_csv_to_json.py", line 136, in main
    rows = read_csv(DEFAULT_CSV_PATH)

File "task1_csv_to_json.py", line 56, in read_csv
    with open(filepath, mode="r", encoding="utf-8-sig", newline="") as csv_file:
```

#### 錯誤原因

程式中的路徑設定是：

```python
DEFAULT_CSV_PATH = "../../113年新生資料庫.csv"
```

目前程式所在位置是：

```text
weeks/week-10/solutions/1114405055/
```

所以 `../../113年新生資料庫.csv` 會指向：

```text
weeks/week-10/113年新生資料庫.csv
```

但是該位置沒有找到 `113年新生資料庫.csv`，因此發生 `FileNotFoundError`。

#### 修正方式：修改 `DEFAULT_CSV_PATH`

如果 CSV 和 `task1_csv_to_json.py` 放在同一層，則將：

```python
DEFAULT_CSV_PATH = "../../113年新生資料庫.csv"
```

改成：

```python
DEFAULT_CSV_PATH = "../../../../assets/stu-data/113年新生資料庫.csv"
```
#### 學到的重點

這次錯誤讓我理解：

1. 相對路徑是根據「執行程式時的工作目錄」判斷，不一定是根據 `.py` 檔案所在位置。
2. 作業中的資料檔應該放在程式預期的位置。
3. 若要讓程式更穩定，應使用 `Path(__file__).resolve().parent` 取得目前 Python 檔案所在資料夾。
4. `FileNotFoundError` 通常不是程式邏輯錯誤，而是檔案位置或路徑設定錯誤。

---

## 本次 AI 協助總結

這次 AI 主要協助我完成：

1. 建立 Week 10 作業專案架構。
2. 撰寫 Task 1 與 Task 2 的 unittest 測試。
3. 分析第一次測試失敗的 Red 階段錯誤。
4. 修正 Task 1 與 Task 2 的核心函式。
5. 確認 14 個測試全部通過。
6. 分析執行 Task 1 時出現的 CSV 路徑錯誤。
7. 整理 `AI_USAGE.md`，記錄 AI 使用方式、採用建議、拒絕建議與錯誤修正案例。
