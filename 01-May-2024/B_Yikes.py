import bisect


n = int(input())
a = list(map(int, input().split()))
k = int(input())
q = list(map(int, input().split()))

for i in range(1, n):
    a[i] += a[i-1]

for j in q:
    print(bisect.bisect_left(a, j)+1)
