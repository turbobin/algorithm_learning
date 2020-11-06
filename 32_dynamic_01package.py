# -*- coding: utf-8 -*-
"""
动态规划：0-1背包问题
对于一组不同重量、不同价值、不可分割的物品，我们选择将某些物品装入背包，
在满足背包最大重量限制的前提下，背包中可装入物品的总价值最大是多少呢？
"""


class Solution:
    def knapsack(self, weights, values, n, w):
        """先用回溯算法+备忘录的方式来解决"""
        # weights:物品重量，values:物品价值，n:物品个数，w:背包可承载重量
        self.max_value = 0
        self.max_weight = 0
        memo = {}

        def _recur_func(i, sw, sv):
            # 已装满或者已选完所有物品
            if i == n or sw == w:
                self.max_value = max(sv, self.max_value)
                self.max_weight = max(sw, self.max_weight)
                return
            item = (i, sw)
            if item in memo and memo[item] > sv:
                # 物品总量相同但是价值更小，舍弃
                return
            memo[item] = sv
            _recur_func(i+1, sw, sv)
            if sw + weights[i] <= w:
                _recur_func(i+1, sw + weights[i], sv + values[i])
        _recur_func(0, 0, 0)
        return self.max_weight, self.max_value

    def knapsack2(self, weights, values, n, w):
        """动态规划解法"""
        states = [[-1] * (w+1) for _ in range(n)]    # 记录每个状态的最大值
        states[0][0] = 0
        if states[0][weights[0]] <= w:
            states[0][weights[0]] = values[0]
        for i in range(1, n):
            for j in range(w+1):
                # 不放入背包
                if states[i-1][j] >= 0:
                    states[i][j] = states[i-1][j]
            k = weights[i]
            for j in range(w-k+1):
                # 放入背包
                if states[i-1][j] >= 0:
                    sv = states[i-1][j] + values[i]     # 前面物品总价值加上当前这个物品价值
                    if sv > states[i][j+k]:
                        states[i][j+k] = sv

        # 找出最大值
        max_value = 0
        sum_weight = 0
        for j in range(w+1):
            if states[n-1][j] > max_value:
                max_value = states[n-1][j]
                sum_weight = j
        return sum_weight, max_value


if __name__ == "__main__":
    weights = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    n = 5
    w = 16
    result = Solution().knapsack(weights, values, n, w)
    print(result)
    result = Solution().knapsack2(weights, values, n, w)
    print(result)
