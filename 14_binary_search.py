# -*- coding: utf-8 -*-

def binary_search(arr, key):
    if len(arr) <= 1:
        return 0

    min = 0
    max = len(arr) - 1
    mid = (min + max) // 2  # 地板除，只保留整数
    while arr[mid] != key:
        if arr[mid] > key:
            max = mid - 1
        elif arr[mid] < key:
            min = mid + 1

        mid = (min + max)//2
        if min > max:
            return None

    return mid


def binary_search2(arr, key):
    """
    二分法，时间复杂度 O(logn)
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            return mid

    return None


def binary_search3(arr, key):
    n = len(arr)
    return _binary_search_recur(arr, 0, n-1, key)

def _binary_search_recur(arr, low, high, key):
    if low > high:
        return None
    mid = low + ((high - low)>>1)
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return _binary_search_recur(arr, mid+1, high, key)
    else:
        return _binary_search_recur(arr, low, mid-1, key)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print('返回数组下标位置：', binary_search(arr, 4))
    print('返回数组下标位置：', binary_search2(arr, 8))
    print('返回数组下标位置：', binary_search3(arr, 5))



