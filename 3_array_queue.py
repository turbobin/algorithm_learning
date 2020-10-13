#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/20'

class ArrayQueue():
    """顺序队列"""
    def __init__(self, capacity: int):
        self.arr = []
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.tail == self.capacity:
            if self.head == 0:
                print('队列满了')
                return False

            # 进行数据搬移
            for i in range(self.head, self.tail):
                self.arr[i - self.head] = self.arr[i]

            # 重新调整指针和数组
            self.tail = self.tail - self.head
            self.head = 0
            self.arr = self.arr[self.head: self.tail]

        self.arr.append(item)
        self.tail += 1
        print('入队:', item)
        return True

    def dequeue(self):
        if self.head == self.tail:
            print('队列空了')
            return None

        item = self.arr[self.head]
        self.head += 1
        # self.arr = self.arr[self.head:]
        print('出队：', item)
        return item

    def __repr__(self) -> str:
        print('指针：', self.head, self.tail)
        return '{}'.format(self.arr[self.head: self.tail])


if __name__ == '__main__':
    arrayqueue = ArrayQueue(5)
    arrayqueue.enqueue(2)
    arrayqueue.enqueue(3)
    arrayqueue.enqueue(4)
    arrayqueue.dequeue()
    arrayqueue.dequeue()
    arrayqueue.enqueue(5)
    arrayqueue.enqueue(6)
    arrayqueue.enqueue(7)
    arrayqueue.enqueue(8)
    arrayqueue.enqueue(9)
    print(arrayqueue)



