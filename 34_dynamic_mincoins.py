# -*- coding: utf-8 -*-
"""
硬币找零问题：
假设我们有几种不同币值的硬币 v1，v2，……，vn（单位是元）。如果我们要支付 w 元，求最少需要多少个硬币。
比如，我们有 3 种不同的硬币，1 元、3 元、5 元，我们要支付 9 元，最少需要 3 个硬币（3 个 3 元的硬币）。
"""

class Solution:
    def back_tracking(self, coins, w):
        """回溯算法解法"""
        # coins 币种数组，w 目标支付金额
        self.min_coins = 0
        memo = {}

        def min_coins(sum_coin, coins_cnt=0):
            if sum_coin == w:
                if self.min_coins == 0:
                    self.min_coins = coins_cnt
                self.min_coins = min(self.min_coins, coins_cnt)
                return

            # 备忘录，记录较小的硬币数
            if sum_coin in memo and coins_cnt > memo[sum_coin]:
                return
            memo[sum_coin] = coins_cnt

            for coin in coins:
                if sum_coin + coin <= w:
                    min_coins(sum_coin + coin, coins_cnt + 1)

        min_coins(0, 0)
        return self.min_coins


    def dynamic_solve(self, coins, w):
        """动态规划解法"""
        # 状态记录当金额为 i 时所需要的最小硬币数
        states = [0] * (w + 1)  # 初始化为0
        for m in range(1, w+1):
            min_coins = float("inf")
            for coin in coins:
                if m >= coin:
                    print(m, coin, states)
                    min_coins = min(min_coins, 1 + states[m-coin])
                else:
                    break
            states[m] = min_coins
        return states[-1]


if __name__ == "__main__":
    coins = [1, 3, 5]
    w = 9
    result = Solution().back_tracking(coins, w)
    print(result)
    result = Solution().dynamic_solve(coins, w)
    print(result)
