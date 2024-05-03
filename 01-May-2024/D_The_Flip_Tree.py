from collections import deque


n = int(input())
g = [[] for _ in range(n)]

for i in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

ina = list(map(int, input().split()))
gol = list(map(int, input().split()))
v = []
for i in range(len(ina)):
    v.append([ina[i], gol[i]])

q = deque([[0, 0, False, False]])
visited = set()
ops = 0
ver = []
while q:
    cu = len(q)
    for j in range(cu):
        lev, node, od, ev = q.popleft()
        if lev % 2 and od:
            v[node][0] = abs(v[node][0]-1)

        if not lev % 2 and ev:
            v[node][0] = abs(v[node][0]-1)

        if v[node][0] != v[node][1]:
            if lev % 2:
                od = not od
            else:
                ev = not ev
            ops += 1
            ver.append(node)

        for nb in g[node]:
            if nb not in visited:
                q.append([lev+1, nb, od, ev])
                visited.add(nb)
print(ops)
for k in range(len(ver)):
    print(ver[k]+1)
