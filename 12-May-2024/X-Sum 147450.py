# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

from collections import defaultdict


for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for i in range(n)]
    d = defaultdict(int)
    for i in range(n):
        for j in range(m):
            d[(1, j-i)] += g[i][j]
            d[(2, j+i)] += g[i][j]

    _max = 0
    for i in range(n):
        for j in range(m):
            _max = max(_max, d[(1, j-i)] + d[(2, j+i)]-g[i][j])

    print(_max)
