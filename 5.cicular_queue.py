#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/21'

class CircularQueue(object):
	"""基于数组实现的循环队列"""
	def __init__(self, capacity):
		self.arr = []
		self.capacity = capacity
		self.head = 0
		self.tail = 0


	def enqueue(self, item):
		n = self.capacity
		if (self.tail + 1)%n == self.head:
			print('队列满了')
			return False
		
		self.arr.append(item)
		self.tail = (self.tail + 1)%n
		return True

	def dequeue(self):
		n = self.capacity
		if self.head == self.tail:
			print('队列空了')
			return False

		item = self.arr[self.head]
		self.head = (self.head + 1)%n
		return item

	def __repr__(self):
		print('指针：', self.head, self.tail)
		if self.head <= self.tail:
			return "{}".format(self.arr[self.head: self.tail])
		else:
			return "{}".format(self.arr[self.head: self.capacity + self.tail])

if __name__ == '__main__':
	Q = CircularQueue(8)
	for i in range(7):	# 实际只能存7个数据，最后一个存tail指针
		Q.enqueue(i)
	print(Q)

	Q.dequeue()
	Q.dequeue()
	Q.dequeue()
	Q.enqueue(7)
	Q.enqueue(8)
	Q.enqueue(9)
	Q.enqueue(10)
	print(Q)
