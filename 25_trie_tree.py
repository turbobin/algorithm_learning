# -*- coding: utf-8 -*-

class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = [None] * 26
        self.is_end_char = False


class Trie:
    def __init__(self):
        self.root = TrieNode("/")

    def insert(self, text):
        """往 Trie 中插入一个字符串"""
        p = self.root
        for c in text:
            index = ord(c) - ord("a")
            if p.children[index] is None:
                new_node = TrieNode(c)
                p.children[index] = new_node
            p = p.children[index]
        p.is_end_char = True

    def find(self, pattern):
        """在 Trie 树中查找字符串"""
        p = self.root
        for c in pattern:
            index = ord(c) - ord("a")
            if p.children[index] is None:
                return False
            p = p.children[index]
        return True if p.is_end_char else False


if __name__ == "__main__":
    trie = Trie()
    trie.insert("hello")
    trie.insert("her")
    trie.insert("hero")
    print(trie.find("her"))
