from random import randint


def three_way_partition(arr, l, r):
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


def quick_sort(arr, left, right):
    if left >= right:
        return
    piv = randint(left, right)
    arr[piv], arr[left] = arr[left], arr[piv]

    lt, gt = three_way_partition(arr, left, right)
    quick_sort(arr, left, lt - 1)
    quick_sort(arr, gt + 1, right)
