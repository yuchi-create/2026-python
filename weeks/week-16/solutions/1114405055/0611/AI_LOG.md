# AI_LOG — Week 16 排序效能實驗室（0611）

學號：1114405055

---

## Stage 1 — `@timeit` 裝飾器

### 我問 AI 什麼

```
幫我設計 timeit 裝飾器的 unittest 測試，函式簽名是 timeit(func)。
規格如下：
1. 被裝飾函式的回傳值不變
2. 用 functools.wraps 保留 __name__ / __doc__
3. 每次呼叫後把耗時（float 秒）記錄到 wrapper.last_elapsed 和 wrapper.records（list 累積）
4. 裝飾器內不准 print

請先給我測試，確認我理解規格後再給實作。
```

### AI 給了什麼

給出 4 個測試：返回值不變、保留 metadata、last_elapsed 為正、records 累積。
但沒有覆蓋「兩個不同函式的 records 彼此獨立」以及「不能有 print 輸出」。

### 我改了什麼

1. 自己補了 `test_no_print_side_effect`——用 `io.StringIO` 捕捉 stdout 驗證無輸出，
   因為規格明確禁止 print，AI 沒有測這條。
2. 自己補了 `test_independent_instances`——分別裝飾兩個函式，確認 records 不共用，
   這是全域變數 vs 實例屬性的關鍵差異，AI 忽略了。

---

## Stage 2 — 三種排序 + benchmark

### 我問 AI 什麼

```
幫我設計 bubble_sort、quick_sort、merge_sort 的共用測試，
三個函式的簽名固定為 def xxx(data: list) -> list。
規格：
- 回傳新 list，不可修改傳入的 list
- 禁用 sorted() / list.sort()（測試裡驗證可以用 sorted 當預期值）
- 用 subTest 讓三個函式共用同一組 test case，不要複製三份

edge case 我自己想：空 list、只有一個元素、全部相同值、已排序、逆序、有負數。
請給測試骨架。
```

### AI 給了什麼

給了含 `test_basic_cases`、`test_empty_list`、`test_random_data_matches_builtin`、
`test_input_not_mutated` 的骨架，有用 subTest 迴圈，符合要求。
但沒有覆蓋「全部相同值」和「逆序」的 edge case。

### 我改了什麼

1. 補了 `test_all_same_elements`——全相同元素是 bubble 早停優化的邊界，
   也是 quick_sort partition 分到全 pivot == mid 的情況，需要明確測試。
2. 補了 `test_reverse_sorted`——最壞情況，是 bubble/quick 的壓力測試。
3. 補了 `test_single_element_list`——確認長度 1 的輸入也能回傳新 list（不改原輸入）。

---

## Stage 3 — 加速實驗

### 我問 AI 什麼

```
我的 quick_sort 在 n=4000 要 0.0036 秒，想用演算法優化壓低。
有兩個方向：
A. median-of-three pivot
B. 小子陣列切換插入排序（cutoff=10）
這兩個可以同時做嗎？請先說明原理，再給我實作。
加速版必須通過和 Stage 2 完全相同的 test_sorts.py，不要另寫測試。
```

### AI 給了什麼

說明了兩種優化的原理：
- median-of-three 減少已排序資料退化到 O(n²) 的機率
- cutoff 配合插入排序利用 cache locality

給出了 `quick_sort_med3` 的實作，策略正確。

### 我改了什麼

1. AI 給的 `_quick_sort_med3_helper` 用了 in-place partition，
   但 `_median_of_three` 回傳的是值不是 index，發現若有重複值時 `while arr[left] < pivot`
   可能停在錯誤位置，我驗證了全重複輸入（`[3]*100`）確認沒問題。
2. 驗收：把 `quick_sort_med3` append 進 `test_sorts.py` 的 `SORT_FUNCTIONS`，
   確認原本 9 個 test case 全數通過（包括 `test_input_not_mutated`）。

---

## Stage 4 — 畫圖

### 我問 AI 什麼

```
幫我設計 plot_results 的測試，函式簽名：
def plot_results(results: dict, out_path: str) -> None
規格：
- 用 matplotlib（Agg backend）畫折線圖
- out_path 不存在時自動建立父目錄
- 輸出必須是合法 PNG
```

### AI 給了什麼

給了用 `tempfile.TemporaryDirectory` + 驗證 PNG 存在且非空的測試。

### 我改了什麼

1. 補了 `test_png_is_valid_png_header`——讀前 4 bytes 驗證 `\x89PNG`，
   因為光驗「檔案存在且非空」不能證明是合法 PNG（可能只是空 bytes）。
2. AI 沒有測試「out_path 父目錄不存在時自動建立」，我補了 `test_output_dir_autocreated`，
   因為 README 規格說路徑可能不存在。

---

## Stage 5 — 安全自掃

### 我問 AI 什麼

```
對照 OpenSSF Secure Coding Guide for Python 的 08/05/03/04 四章，
審查我的 timing.py、sorts.py、benchmark.py、plot.py，
找出至少 3 條安全問題，每條用一個會紅燈的 unittest 測試表達。
同時告訴我哪些條目判定「不適用」及原因。
```

### AI 給了什麼

找出：
1. 08: 檔案未用 with open
2. 04: 使用 pickle 反序列化（CWE-502）
3. 03: make_data 未驗證 n < 0

並建議用 inspect.getsource 掃 source code 的方式測試。

### 我改了什麼

1. 第 2 條測試（pickle）最初寫 `assertNotIn("pickle", src)`，
   但 `load_results` 的 docstring 解釋不用 pickle 的原因時提到了這個字，導致誤判。
   我改為 `assertNotIn("pickle.load", src)`，只禁止呼叫，不禁止提及原因——
   這才是真正的安全規則：不能呼叫 pickle，不是不能討論 pickle。

2. 補了 `test_sorts_does_not_shadow_list`——掃描 sorts.py 有無 `list =`、`sorted =`，
   AI 沒有主動想到這條，是我在讀 08 Coding Standards 時自己發現的。

**AI 加速比（此階段效率）：**
AI 協作讓測試設計時間從預估 30 分鐘壓縮到約 15 分鐘（-50%），
但需要自己驗收邊界條件（pickle 誤判、magic bytes、獨立 records）。

**演算法優化策略：**
median-of-three pivot + 小區間切換插入排序（cutoff=10），
在 n=4000 達到 1.85x 加速（0.003627s → 0.001963s）。

**安全修補筆數：**
找出並測試 5 條適用規則（with open × 2、json not pickle、ValueError 驗證 × 3、no bare except × 2、no shadow builtins）；
判定 1 條不適用（random vs secrets）。
