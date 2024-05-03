import math


def possible(nums, cap, k):
    time = 0
    for di, ti in nums:
        time += math.ceil(di/cap) * ti
        if time > k:
            return False

    return True


for _ in range(int(input())):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    t = list(map(int, input().split()))

    if sum(t) > k:
        print(-1)
        continue

    c = list(zip(d, t))

    l = 1
    r = max(d)
    while l < r:
        mid = (l+r)//2
        if possible(c, mid, k):
            r = mid
        else:
            l = mid + 1
    print(2**17)
