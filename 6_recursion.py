#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/22'

# 1.案例一
depth = 0

def f(n):
    global depth
    depth += 1
    if depth > 500:
        raise RuntimeError('超出递归深度了')
    if n == 1:
        return 1

    return f(n-1) + 1

f = f(500)
print('f(n):', f)
print('depth:', depth)

# 2.案例二
hashmap = {}
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n in hashmap:
        print('f({})重复计算了'.format(n))
        return hashmap[n]
    ret = f(n-1) + f(n-2)
    hashmap[n] = ret
    return ret

f1 = f(6)
print(f1)

# 3.案例一转成非递归代码
def f(n):
    fn = 1
    for i in range(2, n+1):
        fn = fn + 1

    return fn

print(f(100))

# 4.案例二转成非递归代码
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    ret = 0
    pre = 2
    prepre = 1
    for i in range(3, n+1):
        ret = pre + prepre
        prepre = pre
        pre = ret

    return ret

print(f(6))

