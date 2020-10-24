# -*- coding: utf-8 -*-

class UndiGraph:
    """无向图，使用邻接矩阵存储"""
    def __init__(self, v):
        self.v = v
        self.adj = []
        for __ in range(self.v+1):
            self.adj.append([])

    def add_edge(self, s, t):
        """存储边"""
        if s > self.v or t > self.v:
            return "图存储溢出了"
        self.adj[s].append(t)
        self.adj[t].append(s)

    def __getitem__(self, s):
        if s > self.v:
            raise IndexError("no such index")
        return self.adj[s]

    def __repr__(self):
        return str(self.adj)


class DiGraph:
    """有向图"""
    def __init__(self, v):
        self.v = v
        self.adj = []
        for __ in range(self.v+1):
            self.adj.append([])

    def add_edge(self, s, t):
        """存储边"""
        if s > self.v or t > self.v:
            return "图存储溢出了"
        self.adj[s].append(t)

    def __getitem__(self, s):
        if s > self.v:
            raise IndexError("no such index")
        return self.adj[s]

    def __repr__(self):
        return str(self.adj)


if __name__ == "__main__":
    graph = UndiGraph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(1, 4)
    print(graph[2])
    print(graph)

    print("===============")

    graph = DiGraph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(1, 4)
    print(graph[2])
    print(graph)
