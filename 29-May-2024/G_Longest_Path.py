from collections import deque


n, m = map(int, input().split())
degree = [0]*n
dp = [0]*n
graph = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph[y].append(x)
    degree[x] += 1

que = deque()

for i, deg in enumerate(degree):
    if deg == 0:
        que.append(i)

while que:
    cur = que.pop()
    for child in graph[cur]:
        degree[child] -= 1
        dp[child] = max(dp[child], dp[cur]+1)
        if degree[child] == 0:
            que.append(child)

print(max(dp))
