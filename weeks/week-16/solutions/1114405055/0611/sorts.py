"""Stage 2 + Stage 3 — 三種排序實作（含演算法優化版）

禁用 sorted() / list.sort()；一律回傳新 list，不修改傳入資料。

Stage 3 優化策略：
  quick_sort_med3  — median-of-three pivot + 小區間改插入排序（cutoff=10）
  bubble_sort 已含早停優化（O(n) best case）
"""


# ── Stage 2：基本三種排序 ────────────────────────────────────────────────────

def bubble_sort(data: list) -> list:
    result = list(data)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:  # 已排好，提前結束
            break
    return result


def quick_sort(data: list) -> list:
    if len(data) <= 1:
        return list(data)
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    mid = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def merge_sort(data: list) -> list:
    if len(data) <= 1:
        return list(data)
    half = len(data) // 2
    return _merge(merge_sort(data[:half]), merge_sort(data[half:]))


def _merge(left: list, right: list) -> list:
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ── Stage 3：演算法優化版 ────────────────────────────────────────────────────

_INSERTION_CUTOFF = 10  # 小於此長度改用插入排序


def _insertion_sort_inplace(arr: list, lo: int, hi: int) -> None:
    """原地插入排序，操作 arr[lo:hi+1]"""
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1
        while j >= lo and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _median_of_three(arr: list, lo: int, hi: int) -> int:
    """回傳 arr[lo]、arr[mid]、arr[hi] 的中位數值"""
    mid = (lo + hi) // 2
    a, b, c = arr[lo], arr[mid], arr[hi]
    if a <= b <= c or c <= b <= a:
        return b
    if b <= a <= c or c <= a <= b:
        return a
    return c


def _quick_sort_med3_helper(arr: list, lo: int, hi: int) -> None:
    if hi - lo < _INSERTION_CUTOFF:
        _insertion_sort_inplace(arr, lo, hi)
        return
    pivot = _median_of_three(arr, lo, hi)
    left, right = lo, hi
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    _quick_sort_med3_helper(arr, lo, right)
    _quick_sort_med3_helper(arr, left, hi)


def quick_sort_med3(data: list) -> list:
    """median-of-three pivot + 小區間切換插入排序的 quick sort"""
    result = list(data)
    if len(result) > 1:
        _quick_sort_med3_helper(result, 0, len(result) - 1)
    return result
