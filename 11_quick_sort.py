# -*- coding: utf-8 -*-

"""
快速排序，非原地排序
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
    X = []
    Y = []
    Z = []
    for i in range(p, r+1):
        if arr[i] < pivot:
            X.append(arr[i])
        elif arr[i] == pivot:
            Y.append(arr[i])
        else:
            Z.append(arr[i])
    arr[p: r+1] = X + Y + Z
    return len(X+Y) - 1


if __name__ == '__main__':
    arr = [6, 11, 3, 9, 8]
    print(quick_sort(arr))