"""
归并排序
"""

def merge_sort(arr):
    n = len(arr)
    merge_sort_c(arr, 0, n-1)
    return arr

def merge_sort_c(arr, p, r):
    if p >= r:
        # 递归终止条件
        return

    q = (p+r) // 2  # 地板除，保证是整数
    # 分治递归
    merge_sort_c(arr, p, q)
    merge_sort_c(arr, q+1, r)
    # 合并两个有序数组
    merge(arr, p, q, r)

def merge(arr, p, q, r):
    tmp = []
    i, j = p, q+1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    # 判断哪个子数组中有剩余数据
    start, end = (i, q) if i <= q else (j, r)
    # 将剩余数据拷贝到临时数组
    tmp += arr[start: end+1]
    arr[p: r+1] = tmp


if __name__ == '__main__':
    arr = [1, 5, 6, 2, 4, 3]
    print(merge_sort(arr))
