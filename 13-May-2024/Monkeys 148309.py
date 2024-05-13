# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.time = {i: float('inf') for i in range(1, n + 1)}

    def find(self, x):
        if x == self.parent[x]:
            return (x, self.time[x])

        par = self.find(self.parent[x])
        self.time[x] = min(self.time[x], par[1])
        self.parent[x] = par[0]

        return (self.parent[x], self.time[x])

    def union(self, x, y, t):
        px, tx = self.find(x)
        py, ty = self.find(y)

        if px != py:
            if px == 1:
                self.parent[py] = px
                self.time[py] = min(ty, t)
            else:
                self.parent[px] = py
                self.time[px] = min(tx, t)


n, m = map(int, input().split())
edges = []

for i in range(n):
    a, b = map(int, input().split())
    edges.append((a, b))

removed = []
for i in range(m):
    a, b = map(int, input().split())
    removed.append((a, b))

removed_set = set(removed)

ds = UnionFind(n)
for i, (u, v) in enumerate(edges):
    if u != -1 and (i + 1, 1) not in removed_set:
        ds.union(i + 1, u, float('inf'))
    if v != -1 and (i + 1, 2) not in removed_set:
        ds.union(i + 1, v, float('inf'))


removed.reverse()
for i, (u, v) in enumerate(removed):
    ds.union(u, edges[u - 1][v - 1], m - i - 1)

for i in range(1, n + 1):
    if ds.find(i)[1] < float('inf'):
        print(ds.find(i)[1])
    else:
        print(-1)
