# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pre_order(self, root):
        """前序遍历"""
        if not root:
            return
        # 先打印本节点，再打印左节点，最后打印右节点
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.rihgt)

    def in_order(self, root):
        """中序遍历"""
        if not root:
            return
        # 先打印左节点，再打印本节点，后打印右节点
        self.in_order(root.left)
        print(root.val)
        self.in_order(root.right)

    def post_order(self, root):
        if not root:
            return
        # 先打印左节点，再打印右节点，最后打印本节点
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

