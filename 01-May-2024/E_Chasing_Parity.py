from collections import deque


n = int(input())
a = list(map(int, input().split()))
ans = [-1]*n
g = [[]for _ in range(n)]

for i, nm in enumerate(a):
    if i + nm < n:
        g[nm+i].append(i)

    if i - nm > -1:
        g[i-nm].append(i)

q = deque()
visited = set()
for i, nm in enumerate(a):
    if nm % 2:
        q.append(i)
        visited.add(i)

dist = 0
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        if a[curr] % 2 == 0:
            ans[curr] = dist

        for nbr in g[curr]:
            if nbr not in visited:
                q.append(nbr)
                visited.add(nbr)

    dist += 1

visited.clear()
for i, nm in enumerate(a):
    if nm % 2 == 0:
        q.append(i)
        visited.add(i)

dist = 0
while q:
    for _ in range(len(q)):
        curr = q.popleft()
        if a[curr] % 2 == 1:
            ans[curr] = dist

        for nbr in g[curr]:
            if nbr not in visited:
                q.append(nbr)
                visited.add(nbr)
    dist += 1
print(*ans)
