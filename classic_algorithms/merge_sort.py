from typing import List, Optional


def merge(a, b):
    a_len = len(a)
    b_len = len(b)
    res = [None] * (a_len + b_len)
    i = 0
    j = 0
    k = 0
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
    print(f"res = {res}")
    return res


def merge_sort(arr, left: Optional[int] = None, right: Optional[int] = None) -> List:
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    print(f"merge_sort for {arr[left: right + 1]}")

    if left == right:
        print("left = right")
        return arr[left : right + 1]

    if right - left > 0:
        mid = left + (right - left) // 2
        a = merge_sort(arr, left, mid)
        b = merge_sort(arr, mid + 1, right)
        print(f"a and b = {a}, {b}")
        result = merge(a, b)
    else:
        return arr[left : right + 1]
    return result


if __name__ == "__main__":
    ar = [8, 4, 2, 15, 23, 4, 2, 49]
    print(ar)
    ar = merge_sort(ar)
    print(ar)
