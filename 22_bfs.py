# -*- coding: utf-8 -*-

from collections import deque


class Graph:
    """无向图，使用邻接矩阵存储"""

    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(self.v+1)]

    def add_edge(self, s, t):
        """存储边"""
        if s > self.v or t > self.v:
            return "图存储溢出了"
        self.adj[s].append(t)
        self.adj[t].append(s)

    def bfs(self, s, t):
        if s == t:
            return
        visited = [False] * self.v
        visited[s] = True
        queue = deque()
        queue.append(s)
        prev = [-1] * self.v
        while queue:
            print(queue)
            w = queue.popleft()
            for q in self.adj[w]:
                if visited[q]:
                    continue
                prev[q] = w
                if q == t:
                    print(prev)
                    path = self._print_path(prev, s, t)
                    print("->".join(path))
                    return
                visited[q] = True
                queue.append(q)

    def _print_path(self, prev, s, t):
        """递归打印路径"""
        if prev[t] != -1 and s != t:
            yield from self._print_path(prev, s, prev[t])
        yield str(t)

    def __getitem__(self, s):
        if s > self.v:
            raise IndexError("no such index")
        return self.adj[s]

    def __repr__(self):
        return str(self.adj)


if __name__ == "__main__":
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    print(graph)
    graph.bfs(0, 7)
