from random import randint
from typing import Optional, List


def partition_rand(ar: List, l: int, r: int) -> int:
    pivot = randint(l, r)
    ar[l], ar[pivot] = ar[pivot], ar[l]
    return partition(ar, l, r)


def partition(arr: List, l: int, r: int) -> int:
    pivot = l
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def quicksort(arr, left: Optional[int] = None, right: Optional[int] = None) -> None:
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if len(arr) == 1:
        return
    if left < right:
        pi = partition_rand(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)
