# -*- coding: utf-8 -*-

"""
二分查找的变体
"""


def binary_search1(arr, key):
    """查找第一个值等于给定值的元素"""
    n = len(arr)
    if n <= 1:
        return 0

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high-low) >> 1)
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        elif (mid == 0) or (arr[mid-1] != key):
            return mid
        else:
            high = mid - 1  # 注意如果少了这行会导致死循环
    return None


def binary_search2(arr, key):
    """查找最后一个值等于给定值的元素"""
    n = len(arr)
    if n <= 1:
        return 0

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high-low) >> 1)
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        elif (mid == n - 1) or (arr[mid+1] != key):
            return mid
        else:
            low = mid + 1  # 注意如果少了这行会导致死循环
    return None


def binary_search3(arr, key):
    """查找第一个大于等于给定值的元素"""
    n = len(arr)
    if n <= 1:
        return 0

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high-low) >> 1)
        if arr[mid] >= key:
            if (mid == 0) or (arr[mid-1] != key):
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search4(arr, key):
    """查找最后一个小于等于给定值的元素"""
    n = len(arr)
    if n <= 1:
        return 0

    low = 0
    high = n - 1
    while low <= high:
        mid = low + ((high-low) >> 1)
        if arr[mid] <= key:
            if (mid == n - 1) or (arr[mid+1] > key):
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
    print('返回数组下标位置：', binary_search1(arr, 8))
    print('返回数组下标位置：', binary_search2(arr, 8))
    print('返回数组下标位置：', binary_search3(arr, 8))
    print('返回数组下标位置：', binary_search4(arr, 9))
