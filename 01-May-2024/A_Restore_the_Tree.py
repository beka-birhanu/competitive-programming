from collections import deque


n, m = map(int, input().split())
parents = [0]*n
in_degree = parents[:]
g = [[] for _ in range(n)]

for _ in range(m+n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    in_degree[b] += 1
    g[a].append(b)

dq = deque()
for i in range(n):
    if in_degree[i] == 0:
        dq.append(i)

while dq:
    cur = dq.popleft()
    for child in g[cur]:
        in_degree[child] -= 1
        if in_degree[child] == 0:
            parents[child] = cur+1
            dq.append(child)

for parent in parents:
    print(parent)
