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


class Solution2:
    """非递归法实现前、中、后序遍历"""

    def pre_order(self, root):
        """前序遍历"""
        arr = []
        stack = [root]
        while stack:
            root = stack.pop()
            if not root:
                continue
            arr.append(root.val)
            # 先打印左节点，所以需要让左节点先出栈
            stack.append(root.right)
            stack.append(root.left)
        return arr

    def in_order(self, root):
        """中序遍历"""
        arr = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            arr.append(root.val)
            root = root.right
        return arr

    def post_order(self, root):
        """后序遍历"""
        arr = []
        stack = [root]
        # 后序遍历顺序是left -> right -> root
        # 可以利用前序遍历的特点：root -> left -> right 改成 root -> right -> left
        # 顺序正好和后序遍历相反
        while stack:
            root = stack.pop()
            if not root:
                continue
            arr.append(root.val)
            # 让右节点先出栈
            stack.append(root.left)
            stack.append(root.right)
        # 反转数组
        arr.reverse()
        return arr

