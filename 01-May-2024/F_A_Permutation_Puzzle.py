import sys
from math import lcm

for _ in range(int(input())):

    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    lc = 1
    vis = [0] * n
    for i in range(n):
        if vis[i]:
            continue
        cur = []
        ind = i

        while not vis[ind]:
            cur.append(s[ind])
            vis[ind] = 1
            ind = a[ind] - 1

        search = "".join(cur + cur)
        search = search[1:]
        index = search.find("".join(cur)) + 1

        lc = lcm(lc, index)

    print(lc)
