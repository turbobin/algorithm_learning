# -*- coding: utf-8 -*-
"""
动态规划：最短路径长度
一个n x n的矩阵，从最左上角到最右下角经过的数字相加记做路径长度，每次只能向右或
向下移动
"""

class Solution:

    def shortest_path_backtracking(self, matrix):
        """先用回溯算法+备忘录解法"""
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        self.shortest_path = 0
        memo = {}   # 定义备忘录，避免重复计算

        def recur_shortest_path(i, j, sum_path=0):
            if i == n-1 and j == n-1:
                if self.shortest_path == 0 or self.shortest_path > sum_path:
                    self.shortest_path = sum_path
                return
            # 判断坐标是否在备忘录中且数值是否比备忘录的小
            item = (i, j)
            if item in memo and memo[item] <= sum_path:
                return
            memo[item] = sum_path
            if i < n-1:
                # 向下走
                recur_shortest_path(i+1, j, sum_path + matrix[i+1][j])
            if j < n-1:
                # 向右走
                recur_shortest_path(i, j+1, sum_path + matrix[i][j+1])

        recur_shortest_path(0, 0, matrix[0][0])
        return self.shortest_path

    def shortest_path_dynamic(self, matrix):
        """动态规划：状态转移表"""
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        # 状态表，记录到达每个节点的最小值
        states = [[0] * n for _ in range(n)]
        # 第一行数据
        sum_ = 0
        for j in range(n):
            sum_ += matrix[0][j]
            states[0][j] = sum_
        # 第一列数据
        sum_ = 0
        for i in range(n):
            sum_ += matrix[i][0]
            states[i][0] = sum_
        # 填充剩余表格
        for i in range(1, n):
            for j in range(1, n):
                # 当前节点 + 状态表中上节点和左节点中较小的值
                states[i][j] = matrix[i][j] + min(states[i-1][j], states[i][j-1])

        # 状态表中最后一个值就是最小的和
        return states[n-1][n-1]

    def shortest_path_dynamic2(self, matrix):
        """动态规划：状态转移方程"""
        # min_dist(i, j) = w[i][j] + min(min_dist(i, j-1), min_dist(i-1, j))
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        memo = [[0] * n for _ in range(n)]  # 备忘录，避免重复计算

        def recur_min_dist(i, j):
            if i == 0 and j == 0:
                return matrix[0][0]
            print(i, j)

            # 处理角标越界
            if memo[i][j] > 0:
                return memo[i][j]
            min_dist = matrix[i][j] + min(recur_min_dist(i, j-1), recur_min_dist(i-1, j))
            memo[i][j] = min_dist
            return min_dist

        return recur_min_dist(n-1, n-1)


if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 9],
        [2, 1, 3, 4],
        [5, 2, 6, 7],
        [6, 8, 4, 3]
    ]
    result = Solution().shortest_path_backtracking(matrix)
    print(result)
    result = Solution().shortest_path_dynamic(matrix)
    print(result)
    result = Solution().shortest_path_dynamic2(matrix)
    print(result)
