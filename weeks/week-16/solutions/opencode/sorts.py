def _validate_list(data, func_name: str) -> None:
    if data is None:
        raise TypeError(f"{func_name}(): data must be a list, got None")
    if not isinstance(data, list):
        raise TypeError(f"{func_name}(): data must be a list, got {type(data).__name__}")


def bubble_sort(data: list) -> list:
    _validate_list(data, "bubble_sort")
    result = data.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(data: list) -> list:
    _validate_list(data, "quick_sort")
    if len(data) <= 1:
        return data.copy()
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(data: list) -> list:
    _validate_list(data, "merge_sort")
    if len(data) <= 1:
        return data.copy()
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
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
