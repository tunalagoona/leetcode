from random import randint


def partition_rand(ar, left, right):
    pivot = randint(left, right)
    ar[left], ar[pivot] = ar[pivot], ar[left]
    return partition(ar, left, right)


def partition(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def quicksort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition_rand(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
