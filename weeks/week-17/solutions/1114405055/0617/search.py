"""0617 任務二 — 搜尋效能評估

linear_search / binary_search 皆不修改傳入的 data。
"""


def linear_search(data: list, target) -> int:
    """逐一比對 data,找到回傳 index,找不到回 -1。不要求 data 已排序。"""
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


def binary_search(data: list, target) -> int:
    """二分搜尋,前提:data 已排序(由小到大)。

    若 data 實際上未排序,行為未定義——可能找不到本來存在的 target,
    也可能誤判回傳 -1,因為二分搜尋每一步都假設左右兩側已分區。
    本函式不會檢查、也不會排序傳入的 data(維持 O(log n),且不修改傳入物件)。
    """
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
