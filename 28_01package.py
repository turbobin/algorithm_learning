# -*- coding: utf-8 -*-

"""
0-1背包问题：
背包总的承载重量是 Wkg。现在我们有 n 个物品，每个物品的重量不等，并且不可分割。
我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
"""


class Solution:
    def __init__(self, n, w):
        self.n = n  # 多少个物品
        self.w = w  # 背包能装多重
        self.items = [2, 3, 4, 2, 2, 5, 9, 6, 2, 3]     # 每个物品的重量
        self.MAX_W = 0

    def solve(self):

        memo = {}   # 备忘录
        def _recur_package(i, sum_weight):
            if sum_weight == self.w or i == self.n:
                # 已装满或者已选完所有物品
                if sum_weight > self.MAX_W:
                    self.MAX_W = sum_weight
                return
            item = (i, sum_weight)
            if item in memo:
                return  # 已经处理过，不再处理
            memo[item] = True   # 记录状态

            # 不选择第 i 个物品
            _recur_package(i+1, sum_weight)
            if sum_weight + self.items[i] <= self.w:
                # 表示选择第 i 个物品装入背包
                _recur_package(i+1, sum_weight + self.items[i])

        _recur_package(0, 0)
        return self.MAX_W


if __name__ == "__main__":
    result = Solution(10, 37).solve()
    print(result)
