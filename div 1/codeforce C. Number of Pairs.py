import bisect

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        idx = bisect.bisect_left(a, l - a[i], i + 1)
        idx2 = bisect.bisect_right(a, r - a[i], i + 1)
        ans += idx2 - idx
    print(ans)
