# -*- coding: utf-8 -*-

"""
快速排序，原地排序
"""

def quick_sort(arr):
    n = len(arr)
    quick_sort_c(arr, 0, n-1)
    return arr


def quick_sort_c(arr, p, r):
    if p >= r:
        return
    q = partition(arr, p, r)
    quick_sort_c(arr, p, q-1)
    quick_sort_c(arr, q+1, r)


def partition(arr, p, r):
    pivot = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i



if __name__ == '__main__':
    arr = [6, 11, 3, 9, 8]
    print(quick_sort(arr))