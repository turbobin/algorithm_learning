#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/20'

class ArrayStack():
	"""基于数组实现的顺序栈"""
	def __init__(self, n: int):
		self.arr = []
		self.count = 0
		self.n = n

	def push(self, item):
		if self.count == self.n:
			print('栈溢出了', self.arr)
			return False

		self.arr.append(item)
		self.count += 1
		print('push操作：', self.arr)
		return True

	def pop(self):
		if self.count == 0:
			print('栈空了', self.count)
			return None

		item = self.arr[-1]
		self.arr = self.arr[:-1]
		self.count -= 1
		print('pop操作：', item)
		return item

	def __repr__(self):
		return "{}".format(self.arr)

if __name__ == '__main__':
	A = ArrayStack(10)
	A.push(3)
	A.push(1)
	A.push(4)
	print(A)

	A.pop()
	A.pop()
	A.pop()
	A.pop()

	print(A)

