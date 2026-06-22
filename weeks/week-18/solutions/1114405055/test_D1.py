from importlib import import_module

# D1-easy.py 含有破折號不是合法模組名，用 import_module 動態載入
mod = import_module("D1-easy")
process = mod.process

D = 3


def test_sample_1():
    # 核心：去重保序 (4,7,4,2,9,2,6,7 -> 4,7,2,9,6) 後篩選整除 D，再排序
    assert process([4, 7, 4, 2, 9, 2, 6, 7], D) == [6, 9]


def test_sample_2():
    # 核心：無重複值時去重不影響結果，僅驗證篩選與排序
    assert process([1, 3, 5], D) == [3]


def test_edge_case_neg_and_zero():
    # 核心：負數整除判斷 (-3 % 3 == 0)、0 的整除永真特性、負數排序順序
    assert process([-3, -3, 9, 9, -9, 0], D) == [-9, -3, 0, 9]


def test_none_output():
    # 核心：篩選後結果為空列表，process 本身回傳 []，NONE 字串由主程式 I/O 層級負責格式化
    assert process([1, 2, 4, 5, 7], D) == []
