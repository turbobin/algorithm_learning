# -*- coding: utf-8 -*-

import time
def cost_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print("cost_time:", (end - start) * 1000)
        return ret
    return wrapper


class BF:
    """字符串匹配，暴力搜索算法"""

    @cost_time
    def search(self, main, pattern):
        n = len(main)
        m = len(pattern)
        if m > n:
            return -1
        for i in range(n-m+1):
            for j in range(m):
                if main[i+j] != pattern[j]:
                    break
                if j == m - 1:
                    return i
        return -1


class RK:
    """RK 算法，对子串进行哈希"""

    @cost_time
    def search(self, main, pattern):
        n = len(main)
        m = len(pattern)
        hash_pattern = self.hash_string(pattern)
        for i in range(n-m+1):
            ss = main[i:m+i]
            if self.hash_string(ss) != hash_pattern:
                continue
            if ss == pattern:
                return i
        return -1

    def hash_string(self, s):
        """简单哈希法，对每个字符取 Ascii 码值后求和"""
        code = 0
        for c in s:
            code += ord(c)
        return code


if __name__ == "__main__":
    bf = BF()
    index = bf.search("badabcac", "abc")
    print(index)
    rk = RK()
    index = rk.search("badabcac", "abc")
    print(index)

    print("=====Test Time Cost========")
    main = "a" * 10000 + "b"
    pattern = "a" * 1000 + "b"
    print("bf:", bf.search(main, pattern))
    print("rk", rk.search(main, pattern))

