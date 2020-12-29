from typing import List, Optional


def merge(a: List, b: List) -> List:
    a_len = len(a)
    b_len = len(b)
    res = [None] * (a_len + b_len)
    i, j, k = 0, 0, 0

    while i < a_len and j < b_len:
        if a[i] <= b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
        k += 1

    if i < a_len:
        while i != a_len:
            res[k] = a[i]
            i += 1
            k += 1

    if j < b_len:
        while j != b_len:
            res[k] = b[j]
            j += 1
            k += 1
    return res


def merge_sort(arr, left: Optional[int] = None, right: Optional[int] = None) -> List:
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left == right:
        return arr[left : right + 1]

    if right - left > 0:
        mid = left + (right - left) // 2
        a = merge_sort(arr, left, mid)
        b = merge_sort(arr, mid + 1, right)
        result = merge(a, b)
    else:
        return arr[left : right + 1]
    return result
