from collections import Counter, defaultdict

from random import getrandbits

RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(Wrapper, input().split()))
    b = list(map(Wrapper, input().split()))

    c1 = Counter(b)
    c2 = defaultdict(int)

    ans = 0
    bal = 0
    j = 0
    for i in range(n):
        c2[a[i]] += 1
        if c2[a[i]] <= c1[a[i]]:
            bal += 1

        if i - j + 1 > m:
            if c2[a[j]] <= c1[a[j]]:
                bal -= 1
            c2[a[j]] -= 1
            j += 1

        # print(bal, ans, i, j)
        if bal >= k and i - j + 1 == m:
            ans += 1

    print(ans)
