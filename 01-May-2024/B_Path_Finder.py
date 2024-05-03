from heapq import heappop as pop, heappush as push
n = int(input())
g = [[] for i in range(n)]
for _ in range(n-1):
    u, v, d = map(int, input().split())
    g[u].append((v, d))
    g[v].append((u, d))


st = [(0, 0)]
visited = set([0])
_max = 0
while st:
    curr_d, cur_node = pop(st)
    curr_d *= -1
    _max = max(_max, curr_d)
    for nbr, d in g[cur_node]:
        if nbr not in visited:
            push(st, (-(curr_d+d), nbr))
            visited.add(nbr)

print(_max)
