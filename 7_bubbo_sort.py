#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/22'

def bubbo_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    flag = False  # 提前退出冒泡排序的标志
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

        if not flag:  # 表示没有数据交换
            break
    return arr


arr = [4, 5, 6, 1, 2, 3]
arr = bubbo_sort(arr)
print(arr)


class Solution:
    def bubble_sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        for i in range(n-1):
            swap_flag = self.bubble_sort_c(arr, i)
            print(swap_flag)
            if not swap_flag:
                break
        return arr

    def bubble_sort_c(self, arr, i):
        j = 0
        swap_flag = False
        while j < len(arr) - i - 1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
            j += 1
        return swap_flag


if __name__ == "__main__":
    so = Solution()
    arr = [1, 2, 7, 3, 4, 5, 6]
    arr = so.bubble_sort(arr)
    print(arr)
