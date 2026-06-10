"""Stage 2 — 排序正確性測試骨架

規格:sorts.py 的 bubble_sort / quick_sort / merge_sort 必須
  1. 回傳新的排序後 list,不可修改傳入的 list
  2. 禁用內建 sorted() / list.sort()(那是 Stage 3 的對照組)

設計要求:三個函式共用同一組測試——用迴圈 + subTest,不要複製貼上三份。

待辦:
  1. 自己打提示詞跟 AI 討論,補齊測試:
     空 list、單元素、重複值、反向、隨機資料比對、原 list 未被修改
  2. 跑 `python -m unittest` 確認全紅
  3. commit: "test: stage2 排序正確性測試"
  4. 寫 sorts.py,全綠後 commit: "feat: stage2 實作三種排序與 benchmark"
"""

import unittest

# from sorts import bubble_sort, quick_sort, merge_sort  # 完成 sorts.py 後解除註解

# 提示:把三個排序函式放進一個 list,每個測試用
#   for sort_fn in SORT_FUNCTIONS:
#       with self.subTest(sort_fn.__name__):
#           ...
# Stage 3 的加速版只要 append 進這個 list 就能吃到同一組測試。
SORT_FUNCTIONS = []  # 解除上面 import 後填入


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        # 提示:空 list、單元素、重複值、反向排序
        self.fail("尚未實作 — 自己打提示詞跟 AI 討論後補上")

    def test_random_data_matches_builtin(self):
        # 提示:random.seed 固定後產生資料,結果與 sorted() 比對
        #      (測試裡可以用 sorted() 當「驗證標準」,被測函式裡不行)
        self.fail("尚未實作")

    def test_input_not_mutated(self):
        # 提示:排序前先複製一份,排序後驗證原 list 沒變
        self.fail("尚未實作")


if __name__ == "__main__":
    unittest.main()
