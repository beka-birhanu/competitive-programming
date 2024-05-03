import math


def possible(a, j, k):
    left_over = -1
    for p in a:
        if p > j:
            left_over += (p - j)*((100-k)/100)
        if p < j:
            if p + left_over+1 >= j:
                left_over -= j-p
            else:
                return False

    return True


n, k = list(map(int, input().split()))
a = sorted(map(int, input().split()), reverse=True)

ma = a[0]
mi = a[-1]
dif = 1/pow(10, 6)
while ma - mi > dif:
    mid = (mi+ma)/2
    # print(mi, ma, mid, "f")
    if possible(a, mid, k):
        mi = mid + dif

    else:
        ma = mid - dif


print(round(mi, 6))
