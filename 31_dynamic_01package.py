# -*- coding: utf-8 -*-
"""
动态规划：0-1背包问题
背包总的承载重量是 Wkg。现在我们有 n个物品，每个物品的重量不等，并且不可分割。
我们现在期望选择几件物品，装载到背包中。在不超过背包所能装载重量的前提下，如何让背包中物品的总重量最大？
"""


class Solution:
    def knapsack(self, weights, n, w):
        # weights:物品重量，n:物品个数，w:背包可承载重量
        states = [[0] * (w+1) for _ in range(n)]
        states[0][0] = 1    # 第一行数据要特殊处理，利用哨兵
        if weights[0] <= w:
            states[0][weights[0]] = 1
        for i in range(1, n):
            for j in range(w+1):
                if states[i-1][j] == 1:
                    # 不把第i个物品放入背包
                    states[i][j] = states[i-1][j]

            k = weights[i]
            for j in range(w-k+1):
                # 把第i个物品放入背包
                if states[i-1][j] == 1:
                    states[i][j+k] = 1

        # 输出结果，最后一层倒数第一个值为 1 的数据
        while w >= 0:
            if states[n-1][w] == 1:
                return w
            w -= 1
        return 0

if __name__ == "__main__":
    weights = [2, 2, 4, 6, 3]
    n = 5
    w = 9
    result = Solution().knapsack(weights, n, w)
    print(result)



