n = int(input())
g = [[] for _ in range(n)]

e = list(map(int, input().split()))
for u, v in enumerate(e):
    v -= 1
    u += 1
    g[u].append(v)
    g[v].append(u)
c = list(map(int, input().split()))

st = [(0, 0)]
visited = set([0])
ops = 0

while st:
    cur_level = []

    for co, node in st:
        if c[node] != co:
            ops += 1

        for nbr in g[node]:
            if nbr not in visited:
                cur_level.append((c[node], nbr))
                visited.add(nbr)
    st = cur_level
print(ops)
