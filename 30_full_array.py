# -*- coding: utf-8 -*-
"""
回溯算法：全排列问题
从数组中取出 k 个数，有多少种组合方式
"""


class Solution:
    def full_array(self, nums, k):
        arr = [None] * k
        n = len(nums)
        self.cnt = 0

        def _recur_array(k, p=0):
            if k == 0:
                self.cnt += 1
                print(arr)
                return
            for i in range(n-p):
                arr[p] = nums[i]
                nums[i], nums[n-p-1] = nums[n-p-1], nums[i]
                _recur_array(k-1, p+1)
                nums[i], nums[n-p-1] = nums[n-p-1], nums[i]

        _recur_array(k)
        return self.cnt


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 3
    cnt = Solution().full_array(nums, k)
    print(cnt)
