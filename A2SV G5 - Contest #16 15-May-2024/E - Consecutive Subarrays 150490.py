# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

import heapq


n, k = map(int, input().split())
a = list(map(int, input().split()))

p1 = sum(a)
hp = []
curr_sum = 0

for i in range(n-1, 0, -1):
    curr_sum += a[i]
    heapq.heappush(hp, -curr_sum)

for i in range(k-1):
    p1 -= heapq.heappop(hp)

print(p1)