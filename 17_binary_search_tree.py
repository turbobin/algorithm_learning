# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, val=None):
        self.root = TreeNode(val)

    def find(self, val):
        node = self.root
        # 从根节点开始比较每个节点大小
        while node and node.val != val:
            parent = node
            node = parent.left if val < parent.val else parent.right
        return node if node.val == val else None

    def insert(self, val):
        new_node = TreeNode(val)
        if not self.root.val:
            self.root = new_node
            return
        # 寻找插入节点的位置节点
        parent = None
        node = self.root
        while node:
            parent = node
            node = parent.left if val < parent.val else parent.right
        if val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, val):
        # 先查找到这个节点
        node = self.root
        while node and node.val != val:
            parent = node
            node = parent.left if val < parent.val else parent.right
        if not node:
            return
        # 要删除的节点只有一个子节点或没有子节点
        if not all([node.left, node.right]):
            child = node.left if node.left else node.right
            # 更新父节点的指向指向child
            if parent.left == node:
                parent.left = child
            elif parent.right == node:
                parent.right = child
            else:
                self.root = None
        # 要删除的节点有两个节点，先在节点右子树中查找到最小节点
        min_node = node.right
        min_node_parent = node
        while min_node.left:
            min_node_parent = min_node
            min_node = min_node_parent.left
        # 将最小节点替换到被删除节点上
        node.val, min_node.val = min_node.val, node.val
        # 删除这个最小节点
        if min_node_parent.right == min_node:
            # 考虑没有左子节点的情况
            min_node_parent.right = min_node.right
        elif min_node_parent.left == min_node:
            min_node_parent.left = None

    def print_tree(self, root):
        from collections import deque
        res = []
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    row.append(" ")
                    continue
                row.append(node.val)
                q.append(node.left)
                q.append(node.right)
            res.append(row)
        rows = len(res)
        print(res)
        base = 2**(rows)
        for r in range(rows):
            for v in res[r]:
                print(" " * (base), end = "")
                print(v, end = "")
                print(" " * (base - 1), end = "")
            print("")
            base //= 2


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(2)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.print_tree(bst.root)