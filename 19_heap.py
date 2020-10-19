# -*- coding: utf-8 -*-

import heapq

def heap_sort(arr):
    """堆排序"""
    # heapq.heapify(arr)
    tmp = []
    for i in arr:
        heapq.heappush(tmp, i) # 堆化，小顶堆
    print(tmp)
    # 排序，每次取出堆顶元素
    return [heapq.heappop(tmp) for _ in range(len(tmp))]


def merge_sorted_arrs(arr1, arr2, arr3):
    """合并多个有序数组"""
    arr = heapq.merge(arr1, arr2, arr3)
    print(list(arr))


def top_k(arr, k):
    """求top k"""
    topk = heapq.nlargest(k, arr)   # 维护一个小顶堆
    print(topk)
    topk2 = heapq.nsmallest(k, arr)
    print(topk2)


if __name__ == '__main__':
    arr = [1, 5, 9, 8, 2, 3, 4, 7]
    ret = heap_sort(arr)
    print(ret)

    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    arr3 = [6, 7, 8]
    merge_sorted_arrs(arr1, arr2, arr3)
    top_k(arr, 3)

