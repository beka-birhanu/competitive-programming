import math


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    left = math.ceil(k/2)
    right = k//2

    i = 0
    while i < n:
        if a[i] <= left:
            left -= a[i]
            i += 1
        else:
            a[i] -= left
            left = 0
            break

    j = n-1
    while j >= i:
        if a[j] <= right:
            right -= a[j]
            j -= 1
        else:
            break

    rem = j - i + 1
    print(n-rem)
