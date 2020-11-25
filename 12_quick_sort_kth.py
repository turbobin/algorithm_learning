# -*- coding: utf-8 -*-

"""
快速排序，寻找第 K 大元素
"""


def quick_sort(arr, k):
    n = len(arr)
    # 如果是从大到小第 k 个数，转换为求n-k+1
    # k = n - k + 1
    num = quick_sort_c(arr, 0, n-1, k)
    print(num)
    return arr


def quick_sort_c(arr, p, r, k):
    # if p >= r:
    #     return
    q = partition(arr, p, r)
    if q + 1 == k:
        return arr[q]
    if q + 1 > k:
        # 在左半部分查找
        return quick_sort_c(arr, p, q-1, k)
    else:
        # 在右半部分查找
        return quick_sort_c(arr, q+1, r, k)


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
    arr = [6, 11, 3, 1, 9, 2, 8, 7]
    print(quick_sort(arr, 2))
