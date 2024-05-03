import math


n = int(input())
a = sorted(map(int, input().split()))

for i in range(n):
    while a[i] % 2 == 0:
        a[i] //= 2

    while a[i] % 3 == 0:
        a[i] //= 3

for i in range(1, n):
    if a[i] != a[i-1]:
        print("No")
        break

else:
    print("Yes")
