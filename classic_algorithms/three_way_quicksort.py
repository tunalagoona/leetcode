from random import randint
from typing import Optional, List, Tuple


def three_way_partition(arr: List, l: int, r: int) -> Tuple[int, int]:
    lt = l
    i = l
    gt = r
    pivot = arr[l]
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


def quicksort(
    arr: List, left: Optional[int] = None, right: Optional[int] = None
) -> None:
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return
    piv = randint(left, right)
    arr[piv], arr[left] = arr[left], arr[piv]

    lt, gt = three_way_partition(arr, left, right)
    quicksort(arr, left, lt - 1)
    quicksort(arr, gt + 1, right)
