"""Stage 2 — 三種排序實作

禁用 sorted() / list.sort()；一律回傳新 list，不修改傳入資料。
"""


def bubble_sort(data: list) -> list:
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
