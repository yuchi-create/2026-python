# AI_LOG — 排序效能實驗室

## Stage 1 (timeit 裝飾器)

### 我問 AI 什麼
> 讀 README，幫我寫 Stage 1 test_timing.py，規格：timeit(func) 要保留 functools.wraps、f.last_elapsed 為最近一次耗時、f.records 為歷次耗時 list、裝飾器內不准 print。

### AI 給了什麼
> 給了 test_timing.py 內含 6 個測試（含 2 個 edge case：回傳 None 的函式、尚未呼叫前的初始狀態），以及 timing.py 實作。

### 我改了什麼
> 無需修改，直接採用。紅燈 commit 後實作、綠燈通過。

---

## Stage 2 (三種排序 + benchmark)

### 我問 AI 什麼
> 續航，幫我寫 sorts.py：bubble_sort、quick_sort、merge_sort，規格：回傳新 list、不可改輸入、禁用 sorted()/list.sort()。再寫 benchmark.py 量測與 results.json 輸出。測試沿用 test_sorts.py。

### AI 給了什麼
> 給了 sorts.py（三種排序，含 _merge 輔助函式）、benchmark.py（5 種排序 × 4 個 n × 3 次 repeat）、results.json。

### 我改了什麼
> 無需修改，測試全過。紅燈（test: stage2）→ 綠燈（feat: stage2）→ benchmark 補 commit。

---

## Stage 3 (加速方案)

### 我問 AI 什麼
> 續航，實作加速版排序到 sorts_fast.py：bubble 提前停止（一輪沒交換就結束）、quick median-of-three + 小於 16 筆切 insertion sort。測試沿用 test_sorts_fast.py，並補 large_random_data edge case。

### AI 給了什麼
> 給了 sorts_fast.py（bubble_sort_fast、quick_sort_fast、_quick_sort、_median_of_three、_insertion_sort）與 test_sorts_fast.py（含 1000 筆大亂數 edge case）。

### 我改了什麼
> 無需修改，5 個測試全過。

---

## Stage 4 (繪圖輸出)

### 我問 AI 什麼
> 續航，實作 plot.py：load_results 載入 results.json、plot_results 畫圖存 PNG。規格：中文字型、log scale Y 軸、圖例。測試沿用 test_plot.py。

### AI 給了什麼
> 給了 plot.py 含 matplotlib.use("Agg")、FontProperties 指定 macOS 字型、load_results/plot_results 函式。測試 5 個（含 PNG 非空檔、FileNotFoundError edge case）。

### 我改了什麼
> 無需修改，測試全過。紅燈 → 綠燈。

---

## Stage 5 (安全程式碼審查)

### 我問 AI 什麼
> 依 OpenSSF Secure-Coding-Guide-for-Python 審查所有程式碼，找出 major 安全問題並修補。確認：encoding 問題、None 值檢查、型別驗證、寫死路徑。

### AI 給了什麼
> 審查結果：

| # | 問題 | CWE | 受影響檔案 |
|---|---|---|---|
| 1 | 檔案 I/O 未指定 encoding | CWE-176 | benchmark.py line 54, plot.py line 15 |
| 2 | 未檢查 None 值傳入 | CWE-476 | sorts.py / sorts_fast.py 共 5 個排序函式 |
| 3 | 未驗證輸入型別（type confusion） | CWE-843 | sorts.py / sorts_fast.py 共 5 個排序函式 |
| 4 | 寫死 macOS 字型路徑，跨平台失效 | — | plot.py lines 9-11 |

修補內容：
1. `benchmark.py` → `open("results.json", "w", encoding="utf-8")`
2. `plot.py` → `open(path, "r", encoding="utf-8")` + 改用 `plt.rcParams` 動態選字型
3. `sorts.py` → 新增 `_validate_list()`：若 `data is None` 拋 TypeError、非 list 型別拋 TypeError
4. `sorts_fast.py` → 同上，5 個排序函式全部加驗證

### 我改了什麼
> 全部 21 個測試仍全綠。共修補 **3 類安全問題、5 個程式碼點、3 個受影響檔案**，新增測試防禦 `None` 與非法型別傳入。

---

## 加速百分比

n=4000（最大資料量）比較：

| 演算法 | 原始版 (s) | 加速版 (s) | 加速 % |
|--------|-----------|-----------|-------|
| bubble_sort | 0.51783736 | 0.50721720 | 2.05% |
| quick_sort | 0.00406149 | 0.00349183 | **14.03%** |

> quick_sort_fast 因 median-of-three 選 pivot 更穩定 + 小區間切 insertion sort 減少遞迴開銷，在中大型資料（n=4000）加速最顯著（14%）。bubble_sort_fast 的提前停止對亂數資料幫助有限。

## 安全修補統計

| 安全原則 | CWE | 修補點數 |
|---------|-----|---------|
| pyscg-0045 編碼一致性 | CWE-176 | 2 |
| pyscg-0034 None 值檢查 | CWE-476 | 5 |
| pyscg-0011 型別混淆防禦 | CWE-843 | 5 |
| 跨平台字型可攜性 | — | 1 |
| **合計** | | **13 個修補點（3 檔案）** |
