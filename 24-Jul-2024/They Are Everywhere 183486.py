# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import defaultdict


n = int(input())
crs = input()
target = len(set(crs))
count = defaultdict(int)
ans = n

l = 0
for r, cr in enumerate(crs):
    count[cr] += 1
    while l < r and count[crs[l]] > 1:
        count[crs[l]] -= 1
        l += 1

    if len(count) == target:
        ans = min(ans, r-l+1)

print(ans)