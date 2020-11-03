# -*- coding: utf-8 -*-
"""
回溯算法：正则表达式匹配
"""


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.plen = len(pattern)

    def match(self, text):
        self.matched = False
        self.tlen = len(text)
        self.rmatch(0, 0, text)
        return self.matched

    def rmatch(self, ti, pj, text):
        if self.matched:
            return
        if pj == self.plen:
            # 正则表达式到结尾了
            self.matched = True if ti == self.tlen else False
            return
        if self.pattern[pj] == "*":
            # 匹配一个或多个字符，递归搜索每一种情况
            for k in range(self.tlen - ti + 1):
                self.rmatch(ti+k, pj+1, text)
        elif self.pattern[pj] == "?":
            # 匹配一个或0 个任意字符，两种情况
            self.rmatch(ti, pj+1, text)
            self.rmatch(ti+1, pj+1, text)
        elif ti < self.tlen and self.pattern[pj] == text[ti]:
            # 非特殊字符需要精确匹配
            self.rmatch(ti+1, pj+1, text)


if __name__ == "__main__":
    pattern = "ab*eee?d"
    text = "abcdsadfkjlekjoiwjiojieeecd"
    is_match = Pattern(pattern).match(text)
    print(is_match)
