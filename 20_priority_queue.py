# -*- coding: utf-8 -*-
import queue

def test_priority_queue():
    q = queue.PriorityQueue()
    q.put(2)
    q.put(5)
    q.put(1)
    q.put(6)
    q.put(9)
    while not q.empty():
        print(q.get())

def get_topk(nums, k):
    q = queue.PriorityQueue()
    for num in nums:
        q.put(num)
        if q.qsize() > k:
            q.get()
    return q.get()


if __name__ == "__main__":
    test_priority_queue()
    nums = [1, 3, 5, 2, 6, 4]
    k = 2
    print("topk:", get_topk(nums, k))

