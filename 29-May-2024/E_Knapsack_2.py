n, w = map(int, input().split())
vw = sorted(list(map(int, input().split())) for _ in range(n))
max_v = n*max(v for w, v in vw)
dp = [w+1]*(max_v+1)
dp[0] = 0

for wt, v in vw:
    curr = dp[:]
    for vi in range(v, max_v+1):
        curr[vi] = min(curr[vi], dp[vi-v]+wt)

    dp = curr
print(max(idx for idx, weight in enumerate(dp) if weight <= w))
