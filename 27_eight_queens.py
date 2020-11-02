# -*- coding: utf-8 -*-
"""
利用回溯思想解决 8 皇后问题:
我们有一个 8x8 的棋盘，希望往里放 8 个棋子（皇后），每个棋子所在的行、列、对角线都不能有另一个棋子。
"""


class Solution:
    def __init__(self):
        self.result = [-1] * 8
        self.count = 0

    def eight_queens(self, row=0):
        if row == 8:
            # 棋子都放好了，直接打印结果
            self.print_queens()
            self.count += 1
            return
        for col in range(8):
            if not self.is_ok(row, col):  # 检查棋子放法是否满足要求
                continue
            self.result[row] = col
            self.eight_queens(row + 1)
        return self.count

    def is_ok(self, row, col):
        """
        判断row行column列放置是否合适
        1. 同一行是否有棋子
        2. 对角线是否有棋子(行和列间距相等)
        """
        leftup = col - 1
        rightup = col + 1
        i = row - 1
        while i >= 0:
            if self.result[i] == col:    # 第 i 行是否有棋子
                return False
            if leftup >= 0:
                if self.result[i] == leftup:    # 检查左上角
                    return False
            if rightup < 8:
                if self.result[i] == rightup:   # 检查右下角
                    return False
            i -= 1
            leftup -= 1
            rightup += 1
        return True

    def print_queens(self):
        for row in range(8):
            for col in range(8):
                if self.result[row] == col:
                    print("Q ", end="")
                else:
                    print("* ", end="")
            print("")
        print("")


if __name__ == "__main__":
    result = Solution().eight_queens(0)
    print(result)
