#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created on '2019/1/20'

class Node():
    """链表结点和 next 指针"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedStack():
    """基于链表实现的栈"""
    def __init__(self):
        self.base_node = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.base_node
        self.base_node = new_node

    def pop(self):
        if self.base_node:
            item = self.base_node.data
            self.base_node = self.base_node.next	# 表示删除一个结点
            return item
        return None

    def __repr__(self):
        base_node = self.base_node
        items = []
        while base_node:
            items.append(base_node.data)
            base_node = base_node.next

        return "->".join(str(item) for item in items)


if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    item = stack.pop()
    print(item)
    print(stack)
