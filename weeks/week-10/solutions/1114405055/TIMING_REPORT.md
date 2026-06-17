# TIMING_REPORT

## timeit 執行結果

```text
[timeit] read_csv 耗時 0.003385s
[timeit] write_json 耗時 0.005483s
JSON 已儲存：output/students.json
[timeit] read_json 耗時 0.001577s
[timeit] write_xml 耗時 0.003819s
XML 已儲存：output/students.xml
```

---

## 問題回答

### 1. 哪個操作最耗時？你認為原因是什麼？

本次測試中，`write_json` 最耗時，耗時約 `0.005483s`。

我認為主要原因不是因為 `write_json()` 負責從 CSV 中篩選資料，而是因為資料在前面的流程中已經透過 `filter_by_admission()`、`count_by_dept()` 與 `build_output_data()` 整理完成。`write_json()` 的主要工作是將整理好的完整 Python dict 轉換成 JSON 格式，並實際寫入 `students.json` 檔案。

另外，程式在輸出 JSON 時使用了 `ensure_ascii=False` 讓中文可以正常顯示，也使用 `indent=2` 讓 JSON 檔案更容易閱讀。這些格式化處理會讓輸出內容變得比較完整、可讀，但也可能增加一些序列化與寫檔時間。因此在本次執行結果中，`write_json` 成為耗時最久的操作。

---

### 2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

本次測試中，`read_csv` 耗時約 `0.003385s`，`read_json` 耗時約 `0.001577s`，所以 `read_csv` 比 `read_json` 慢。

我認為原因是 CSV 是純文字表格格式，程式需要透過 `csv.DictReader` 逐列讀取資料，並將每一列轉換成 dictionary。相較之下，JSON 本身已經是結構化資料格式，使用 `json.load()` 後可以直接轉成 Python 的 dict 或 list，因此讀取與轉換流程相對簡單。

所以本次結果與課堂 U01 中「讀取結構化資料時，JSON 通常比 CSV 更方便，也可能更快」的觀察大致一致。

---

### 3. write_xml 比 write_json 快還是慢？原因為何？

本次測試中，`write_xml` 耗時約 `0.003819s`，`write_json` 耗時約 `0.005483s`，所以本次結果是 `write_xml` 比 `write_json` 快。

不過，這不代表 XML 在所有情況下都一定比 JSON 快。這次可能是因為 JSON 輸出時包含完整的資料結構，並使用 `indent=2` 進行格式化，輸出內容較完整且可讀性較高，因此寫入時間較長。而 XML 雖然需要建立 ElementTree 結構，但本次輸出的 XML 結構相對單純，主要是將每筆學生資料轉成 `<student>` 標籤與屬性，所以實際耗時比 `write_json` 短。

因此，我認為這次 `write_xml` 比 `write_json` 快，可能與輸出內容大小、格式化方式、資料結構複雜度以及當下電腦執行狀態有關。

---

### 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

如果資料筆數從 100 增加到 10000，我預期四個函式的耗時都會明顯增加，而且大致會隨著資料量成長而增加。

`read_csv` 需要讀取更多列資料，並將每一列轉成 dictionary，因此資料筆數增加時，讀取與解析時間會變長。`read_json` 也會因為 JSON 檔案變大，需要載入更多資料，所以耗時也會增加。

`write_json` 和 `write_xml` 的耗時也會增加，因為兩者都需要輸出更多資料到檔案中。其中 `write_json` 需要將完整 Python dict 序列化成 JSON 文字；`write_xml` 則需要建立更多 `<student>` 節點並寫入 XML 檔案。

如果資料量變成 10000 筆，我預期寫入類操作可能會比讀取類操作更明顯受到影響，因為輸出時除了資料轉換外，還包含檔案寫入、格式化與儲存成本。
