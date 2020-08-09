#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/20'
class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedQueue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        return True
    
    def dequeue(self):
        if self.head:
            item = self.head.data
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return item
    
    def __repr__(self):
        items = []
        base_node = self.head
        while base_node:
            items.append(base_node.data)
            base_node = base_node.next
        return "->".join(str(item) for item in items)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(5):
        q.enqueue(i)
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("5")
    q.enqueue("6")
    print(q)
