# AI_USAGE.md

## 使用工具

- **Claude Code (claude-sonnet-4-6)**：協助完成本作業的程式撰寫、測試與報告整理。

## 使用方式說明

1. **需求理解**：讀取 `HOMEWORK.md` 規格、CSV 資料欄位，以及課堂參考圖（V01/V02/V03）以了解作業要求與風格。
2. **測試撰寫（Red Phase）**：先撰寫 `tests/test_task1.py`、`tests/test_task2.py` 共 10 個測試函式，確認在尚未實作功能模組時測試全部失敗（10 errors，`ModuleNotFoundError`）。
3. **實作撰寫（Green Phase）**：實作 `task1_grouped_bar.py`（並排長條圖）與 `task2_zipcode_heatmap.py`（縣市熱力圖），過程中修正了講義範例中郵遞區號 950–953 重複對應屏東縣/台東縣的問題，最終 10 個測試全部通過。
4. **視覺調整**：圖表配色、格線、標題格式參考課堂範例圖；中文字型自動偵測 Microsoft JhengHei / Arial Unicode MS。
5. **報告撰寫**：根據程式實際計算出的數據（食品科學系跨幅 28 人、澎湖縣 6.6%、台中市 15.6%、六年降幅 40%）撰寫 `REPORT.md`。

## 反思

AI 在「測試先行 → 實作 → 圖表 → 文件」的結構化流程中效率很高，但程式內計算出的數字仍需自行核對是否合理，並由自己補上對數據的觀察與推論，而不是單純接受 AI 給的初稿結論。
