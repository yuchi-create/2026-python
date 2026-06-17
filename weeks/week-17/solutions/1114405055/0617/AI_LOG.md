# AI_LOG — 0617

## 我問 AI 什麼

> TODO:把你自己打的提示詞逐字貼在這裡(本教案規則:提示詞自己打,不提供範例)。

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
>
> TODO:這裡必須由你自己填——例如你檢查了哪段程式碼、發現了什麼問題、做了什麼決定
> (留白或寫「沒改」依規則本項記 0 分)。
