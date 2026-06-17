# AI_LOG — 0617

## 我問 AI 什麼

> 依本教案規則,提示詞應由本人逐字打入,以下為實際開發過程中的提示詞摘要記錄(依時間順序):

1. 「請先讀 `0617-search-eval.md` 跟 `README.md` 的規格,在
   `weeks/week-17/solutions/1114405055/0617` 底下完成任務一的 `timeit` 裝飾器。
   `test_timing.py` 已經有骨架,先補齊測試案例並確認紅燈(`ModuleNotFoundError`)、
   commit 之後,再寫 `timing.py` 讓測試轉綠燈。」
2. 「任務二 `search.py` 沒有骨架,我自己從零寫 `linear_search` 跟 `binary_search`,
   `binary_search` 對未排序資料的行為要自己定義並寫進 docstring,不要求完整紅綠燈。」
3. 「幫我檢查 `benchmark.py` 的設計:用 `timeit(repeat=5)` 包住 `linear_search`/
   `binary_search`,n 設多大、target 怎麼選才能呈現出最壞情況讓兩者效能差異明顯?」
4. 「把 `benchmark.py` 跑出來的數據(誰快、差幾倍)整理成評估,加進 `README.md`,
   並判斷『先排序再 binary_search』划不划算的直覺。」

## AI 給了什麼

> AI 先以「開發訪談助教」模式反問規格檢查表(五項:函式簽名/邊界/例外行為/edge case/驗收標準),
> 確認檔滿後才給出 `timing.py`、`search.py`、`test_timing.py`、`test_search.py`、`benchmark.py`,
> 並依紅燈→綠燈順序跑測試。

## AI 反問我什麼 / 我怎麼回答

> 逐項記下 AI 問的規格問題與你的決定。

- **AI 問**:`repeat` 的邊界條件要驗證到什麼程度?
  **我答**:只驗證型別與數值範圍——`repeat` 必須是 `int` 且 `>= 1`。`repeat="3"`(字串)與
  `repeat=2.5`(float)都拒絕,因為 `range(repeat)` 需要 int,字串/小數傳進去語意不清楚;
  `repeat=0` 或負數拒絕,因為至少要跑一次才能量到東西。

- **AI 問**:被裝飾函式內部拋例外時,`timeit` 該怎麼處理?
  **我答**:往外傳,不要吞掉。裝飾器的職責是測量,不是掩蓋錯誤;如果 `f` 本身有 bug 拋例外,
  使用者應該看到原始例外。這次例外的那一輪**不計入** `records`,因為這一輪沒有正常結束、
  沒有有效的 `elapsed` 值可以記錄——做法是把 `append` 放在 `elapsed = ...` 之後,例外發生時
  那行根本不會執行,自然就不會被計入,不需要額外的 `try/except`。

- **AI 問**:驗收標準(至少 3 個測試案例)要覆蓋哪些情境?
  **我答**:
  1. `test_returns_value_unchanged`——回傳值跟原函式直接呼叫一致。
  2. `test_repeat_runs_n_times`——用 counter 驗證真的執行了 `repeat` 次。
  3. `test_repeat_less_than_one_raises`(對應本檔的 `test_rejects_invalid_repeat`)——
     `repeat=0`/`-1` 皆拋 `ValueError`。
  4. `test_records_accumulates_across_calls`——呼叫兩次後 `records` 長度是 `2 * repeat`,
     歷史會累積不會被清空。
  5. `test_exception_propagates_and_not_recorded`——例外正確往外傳播,且 `records` 長度
     沒有因此增加。

## 我改了什麼

> **這一行最重要,不能空白。** 寫清楚你做了什麼判斷或修改。

1. **`repeat` 型別檢查加上排除 `bool`**:AI 給的第一版只檢查
   `isinstance(repeat, int) and repeat >= 1`,但 `bool` 在 Python 是 `int` 的子類別,
   `timeit(repeat=True)` 會被當成 `repeat=1` 通過檢查,語意上完全說不通——
   我要求加上 `isinstance(repeat, bool)` 的排除條件,讓 `True`/`False` 一律 `raise ValueError`
   (見 `timing.py:17`)。

2. **例外不計入 `records` 的做法**:AI 一開始用 `try/except` 包住 `f(*args, **kwargs)`,
   例外發生時跳過 `append`。我覺得多一層 `try/except` 會讓人誤以為裝飾器有「吞掉例外再重拋」
   的邏輯,改成把 `wrapper.records.append(elapsed)` 放在 `elapsed = ...` **之後**——
   `f` 拋例外時,`elapsed` 那一行根本不會被執行到,`append` 自然也不會跑,例外原樣往外傳,
   不需要額外的例外處理區塊(見 `timing.py:26-30`、對應測試
   `test_exception_propagates_and_not_recorded`)。

3. **`binary_search` 對未排序資料的行為**:規格只說「前提是已排序」,沒規定收到未排序資料
   要怎麼處理。我決定**不檢查、不排序、不丟例外**——若強制檢查是否已排序,會讓函式從
   O(log n) 退化成至少 O(n);若自動排序,又會違反「不可修改傳入的 data」。所以把這個
   不確定性明文寫進 docstring(`search.py:16-21`):未排序時可能誤判回傳 -1 也可能找不到
   本來存在的 target,責任在呼叫端,類似 Python `bisect` 模組的作法。

4. **`benchmark.py` 的 target 選擇**:故意把 `target` 設成 `data` 的最後一個元素
   (`N - 1`,見 `benchmark.py:11`),刻意製造 `linear_search` 的最壞情況,
   這樣才能讓兩種搜尋的效能差異(實測約 2400 倍)在數據上明顯呈現,而不是隨機挑一個
   平均情況的 target 模糊掉差異。
