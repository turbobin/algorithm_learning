# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "TreeNode({})".format(self.val)


class BinarySearchTree:
    def __init__(self, val=None):
        self.root = TreeNode(val)

    def find(self, val):
        node = self.root
        # 从根节点开始比较每个节点大小
        path = ""
        while node and node.val != val:
            path += "{}->".format(node)
            parent = node
            node = parent.left if val < parent.val else parent.right
        path += str(node)
        print(path)
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
        while node.val and node.val != val:
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
        else:
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

    def _build_tree_string(self, root, curr_index, index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.val)
        else:
            node_repr = str(root.val)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = \
            self._build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            self._build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def __repr__(self):
        lines = self._build_tree_string(self.root, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(5)
    bst.insert(8)
    bst.insert(7)
    # bst.delete(8)
    print(bst.find(7))
    print(bst)