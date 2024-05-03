import sys
from collections import deque


class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, i):
        while self.parents[i] != i:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]

        return i

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == b_parent:
            return False

        self.parents[b_parent] = a_parent
        return True


def dfs(src, dst, p, path, g):
    if src == dst:
        path.append(src+1)
        return path

    for nbr in g[src]:
        if nbr == p:
            continue

        if dfs(nbr, dst, src, path, g):
            path.appendleft(src+1)
            return path

    return path


for _ in range(int(input())):
    n, m = map(int, input().split())
    edges = []
    g = [[] for i in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1))

    edges.sort(reverse=True)
    dsu = DSU(n)
    last_cycle = None
    best = 0

    for w, u, v in edges:
        if not dsu.union(u, v):
            last_cycle = (u, v)
            best = w
        else:
            g[u].append(v)
            g[v].append(u)

    ans = dfs(last_cycle[0], last_cycle[1], - 1, deque(), g)
    print(best, len(ans))
    print(*ans)
