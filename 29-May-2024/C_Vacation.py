n = int(input())
a = list(list(map(int, input().split())) for _ in range(n))

for i in range(n-1):
    a[i+1][0] += max(a[i][1], a[i][2])
    a[i+1][1] += max(a[i][0], a[i][2])
    a[i+1][2] += max(a[i][0], a[i][1])

print(max(a[-1]))