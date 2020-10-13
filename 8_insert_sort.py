#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/23'

def insert_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > value:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = value

    return arr

arr = [4, 5, 6, 1, 2, 3]
arr = insert_sort(arr)
print(arr)