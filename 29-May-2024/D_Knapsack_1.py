n, w = map(int, input().split())
vw = sorted(list(map(int, input().split())) for _ in range(n))
dp = [0]*(w+1)

for wt, v in vw:
    curr = dp[:]
    for wei in range(wt, w+1):
        curr[wei] = max(curr[wei], dp[wei-wt]+v)

    dp = curr
print(dp[-1])
