# -*- coding: utf-8 -*-

"""
利用归并排序分治思想求解数组中逆序对的个数
如：[2, 4, 3, 1, 5, 6]
逆序对为：(2, 1), (4, 3), (4, 1), (3, 1)
"""
class Solution:
    def count(self, nums):
        n = len(nums)
        self.cnt = 0
        self.merge_sort_count(nums, 0, n-1)
        print("满有序度：", n * (n-1) / 2)
        print("逆序度：", self.cnt)
        print("有序度:", n * (n-1) / 2 - self.cnt)
        return self.cnt

    def merge_sort_count(self, nums, p, r):
        if p >= r:
            return
        q = p + (r - p) // 2
        self.merge_sort_count(nums, p, q)
        self.merge_sort_count(nums, q+1, r)
        self.merge(nums, p, q, r)

    def merge(self, nums, p, q, r):
        tmp = []
        i, j = p, q+1
        while i <= q and j <= r:
            if nums[i] > nums[j]:
                self.cnt += (q-i+1)     # i 到 q 之间的逆序对个数
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1

        # 判断哪个子数组中还有数据
        start, end = (i, q) if j > r else (j, r)
        tmp = tmp + nums[start: end+1]
        nums[p: r+1] = tmp


if __name__ == "__main__":
    nums = [4, 3, 2, 5, 1, 6]
    result = Solution().count(nums)
    print(result)
