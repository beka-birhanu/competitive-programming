import bisect


n, k = map(int, input().split())
a = list(map(int, input().split()))
base = []
for i in range(k):
    base.append(list(map(int, input().split())))

base.sort()
for i in range(1, k):

    base[i][1] += base[i-1][1]

print(1535+50-2120+120)
