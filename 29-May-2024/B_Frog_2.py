n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [float('inf')]*n
dp[0] = 0
for i in range(n):
    for j in range(i+1, min(n, i+k+1)):
        dp[j] = min(dp[j], dp[i] + (abs(a[j] - a[i])))

print(dp[-1])
