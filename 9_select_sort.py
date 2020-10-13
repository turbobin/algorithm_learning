#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/16'

def findmin(arr):
    """
    找出数组中最小值
    """
    min_num = arr[0]
    min_index = 0
    n = len(arr)
    for i in range(1, n):
        if arr[i] < min_num:
            min_num = arr[i]
            min_index = i

    return min_index


def select_sort(arr):
    """
    快速排序，时间复杂度 O(n^2)
    """
    new_arr = []
    for i in range(len(arr)):
        min_index = findmin(arr)
        new_arr.append(arr.pop(min_index))

    return new_arr


arr = [3, 5, 1, 6, 0, 6]
# print(findmin(arr))
print(select_sort(arr))


# 选择排序2
def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n):
        min_index = i
        min_val = arr[i]
        for j in range(i, n):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [3, 5, 1, 6, 0, 6]
arr = selection_sort(arr)
print(arr)