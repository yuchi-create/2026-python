"""Stage 3 — 三種排序的獨立優化版本

策略：
  bubble_sort_fast  — 早停機制（early stop）
  quick_sort_fast   — 中間元素 pivot，避免已排序退化
  merge_sort_fast   — 迭代式 bottom-up merge，消除遞迴堆疊開銷
"""


def bubble_sort_fast(data: list) -> list:
    """早停 bubble sort：某趟若無交換則已排好，立即結束"""
    result = list(data)
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def _partition_mid(arr: list, lo: int, hi: int) -> int:
    """以中間元素為 pivot 進行 in-place partition，回傳 pivot 最終位置"""
    mid = (lo + hi) // 2
    arr[mid], arr[hi] = arr[hi], arr[mid]  # 把 pivot 移到末尾
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def _quick_sort_fast_helper(arr: list, lo: int, hi: int) -> None:
    if lo < hi:
        p = _partition_mid(arr, lo, hi)
        _quick_sort_fast_helper(arr, lo, p - 1)
        _quick_sort_fast_helper(arr, p + 1, hi)


def quick_sort_fast(data: list) -> list:
    """中間 pivot quick sort，減少已排序資料退化到 O(n²) 的機率"""
    result = list(data)
    if len(result) > 1:
        _quick_sort_fast_helper(result, 0, len(result) - 1)
    return result


def _merge_inplace(arr: list, lo: int, mid: int, hi: int) -> None:
    """合併兩段已排序子陣列 arr[lo:mid+1] 與 arr[mid+1:hi+1]"""
    left = arr[lo:mid + 1]
    right = arr[mid + 1:hi + 1]
    i = j = 0
    k = lo
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort_fast(data: list) -> list:
    """迭代式 bottom-up merge sort，消除遞迴呼叫的堆疊開銷"""
    result = list(data)
    n = len(result)
    width = 1
    while width < n:
        for lo in range(0, n, width * 2):
            mid = min(lo + width - 1, n - 1)
            hi = min(lo + width * 2 - 1, n - 1)
            if mid < hi:
                _merge_inplace(result, lo, mid, hi)
        width *= 2
    return result
