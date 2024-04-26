# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [set() for j in range(n)]
    in_deg = [0]*n
    e = set()
    for j in range(m):
        t, x, y = map(int, input().split())
        x -= 1
        y -= 1

        if t == 1:
            g[x].add((1, y))
            e.add((x, y))
            in_deg[y] += 1

        else:
            g[x].add((0, y))
            g[y].add((0, x))

    dq = deque()
    for i in range(n):
        if in_deg[i] == 0:
            dq.append(i)
    count = 0
    while dq:
        cur = dq.popleft()
        count += 1
        for t, nbr in g[cur]:
            if t == 1:
                in_deg[nbr] -= 1
                if in_deg[nbr] == 0:
                    dq.append(nbr)
            else:
                g[nbr].remove((0, cur))
                e.add((cur, nbr))

    if count != n:
        print("NO")
        continue

    print("YES")
    for x, y in e:
        print(x+1, y+1)
