# AI_LOG — 6/10 數字根

## 我問 AI 什麼

請幫我用 Python unittest 為 digit_root(n) 函式寫測試，至少包含：基本多位數案例（如 199→1、24→6）、edge case（一位數直接回傳、極大值 2000000000）、以及 n<1 應 raise ValueError("n must be >= 1") 的例外案例。

## AI 給了什麼

提供了 test_basic（24→6）、test_single_digit（5→5）、test_invalid（n=0 raise ValueError）三個案例，但沒有覆蓋大數邊界、負數輸入，也沒有驗證 ValueError 的訊息文字是否完全吻合。

## 我改了什麼

1. 新增 `test_basic_multi_step`（199→1）和 `test_basic_nine`（9999→9）補充多步驟收斂的案例。
2. 新增 `test_edge_large_number`（2_000_000_000→2）確認上限值不會溢位或超時。
3. 把 `assertRaises` 改用 `ctx.exception` 驗證錯誤訊息字串，因為題目要求「一字不差」，光 assertRaises 不夠。
4. 新增 `test_invalid_negative_raises`（n=-5），AI 只測 n=0，漏掉負數也應觸發例外。
