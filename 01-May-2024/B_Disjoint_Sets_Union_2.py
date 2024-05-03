def find(parents, i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]

    return i


n, m = map(int, input().split())
p = [i for i in range(n)]
g = [[i+1, i+1, 1] for i in range(n)]

for _ in range(m):
    q = input()

    if q[0] == "u":
        _, x, y = q.split()
        x = int(x)-1
        y = int(y)-1

        px = find(p, x)
        py = find(p, y)
        if px != py:
            p[px] = py
            g[py][0] = min(g[px][0], g[py][0])
            g[py][1] = max(g[px][1], g[py][1])
            g[py][2] += g[px][2]

    else:
        _, x = q.split()
        x = int(x)-1
        px = find(p, x) 

        print(*g[px])
