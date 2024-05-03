from heapq import heappop as pop, heappush as push


n, c = map(int, input().split())
g = [[] for _ in range(n)]
d = [0] * n

for _ in range(c):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    d[b-1] += 1

hp = []
for i in range(n):
    if d[i] == 0:
        hp.append(i)

ans = []
while hp:
    lett = pop(hp)
    ans.append(str(lett+1))

    for nxt in g[lett]:
        d[nxt] -= 1
        if d[nxt] == 0:
            push(hp, nxt)

print(" ".join(ans)) if len(ans) == n else print(-1)
