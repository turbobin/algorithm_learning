# -*- coding: utf-8 -*-

"""
计数排序
"""

def count_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    # 获取数组的范围
    max_num = max(arr)
    # 申请一个大小为 max_num 的初始化数组
    C = [0] * (max_num + 1)
    # 计算每个元素的个数
    for i in arr:
        C[i] += 1
    # 依次累加
    for j in range(1, max_num+1):
        C[j] = C[j-1] + C[j]
    # 临时数组 R，存储排序后的结果
    R = [None] * n
    # 倒叙遍历，计数得出元素的排序位置
    for k in arr[::-1]:
        index = C[k] - 1
        R[index] = k
        C[k] -= 1
    return R


if __name__ == '__main__':
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    print(count_sort(arr))