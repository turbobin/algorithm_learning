#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/13'


def binary_search(arr, key):
	if len(arr) <= 1:
		return 0
	arr.sort()
	print(arr)

	min = 0
	max = len(arr) - 1
	mid = (min + max)//2	# 地板除，只保留整数
	print(mid)
	while arr[mid] != key:
		if arr[mid] > key:
			max = mid - 1
		elif arr[mid] < key:
			min = mid + 1
		
		mid = (min + max)//2
		if min > max:
			return None

	return mid


def binary_search2(arr, key):
	"""
	二分法，时间复杂度 O(logn)
	"""
	arr.sort()
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2
		if arr[mid] > key:
			high = mid - 1
		elif arr[mid] < key:
			low = mid + 1
		else:
			return mid

	return None



arr = [3, 1, 4, 5, 2]
print('返回数组下标位置：', binary_search(arr, 4))
print('返回数组下标位置：', binary_search2(arr, 8))




