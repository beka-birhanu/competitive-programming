from math import gcd


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tot = 0
    pos = 0
    zero = 0
    neg = 0
    for i in range(n):
        a[i] -= k
        tot += a[i]
        if a[i] > 0:
            pos = 1
        elif a[i] == 0:
            zero = 1
        else:
            neg = 1

    if pos + zero + neg >= 2:
        print(-1)
        continue

    if zero == 1:
        print(0)
        continue

    g = 0
    for i in range(n):
        g = gcd(g, abs(a[i]))

    ans = abs(tot) // g - n
    print(ans)
