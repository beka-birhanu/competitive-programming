# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

recipes_temp = [0]*200002
n, k, q = map(int, input().split())

for _ in range(n):
    l, r = map(int, input().split())
    recipes_temp[l] += 1
    recipes_temp[r+1] -= 1

for i in range(1, 200002):
    recipes_temp[i] += recipes_temp[i-1]
    recipes_temp[i-1] = 1 if recipes_temp[i-1] >= k else 0


for i in range(1, 200002):
    recipes_temp[i] += recipes_temp[i-1]

for i in range(q):
    a, b = map(int, input().split())
    count = recipes_temp[b] - recipes_temp[a-1]
    print(count)