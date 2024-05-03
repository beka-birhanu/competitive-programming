import bisect
from collections import deque


def merge(left, right):
    merged_arr = []
    l, r = 0, 0
    lff = [p for i, p in left]
    rff = [p for i, p in right]
    # print(left, right)
    while l < len(left) and r < len(right):
        if left[l][1] < right[r][1]:
            x = left[l][:]
            x[1] += bisect.bisect_left(rff,
                                       left[l][1])
            merged_arr.append(x)
            l += 1

        elif left[l][1] > right[r][1]:
            x = right[r][:]
            x[1] += bisect.bisect_left(lff,
                                       right[r][1])
            merged_arr.append(x)
            r += 1

        else:
            x = left[l][:]
            x[1] += bisect.bisect_left(rff,
                                       left[l][1])
            y = right[r][:]
            y[1] += bisect.bisect_left(lff,
                                       right[r][1])
            if x[1] < y[1]:

                merged_arr.append(x)
                l += 1
            else:

                merged_arr.append(y)
                r += 1

        # print(merged_arr)
    while l < len(left):
        x = left[l][:]
        x[1] += bisect.bisect_left(rff,
                                   left[l][1])
        merged_arr.append(x)
        l += 1

    while r < len(right):
        x = right[r][:]
        x[1] += bisect.bisect_left(lff,
                                   right[r][1])
        merged_arr.append(x)
        r += 1
    merged_arr.sort(key=lambda x: x[1])
    # print(merged_arr,  '\n')
    return merged_arr


for _ in range(int(input())):
    n = 2**int(input())
    a = list(map(int, input().split()))
    b = deque()

    for i, p in enumerate(a):
        b.append([[i, p]])
    a = b
    while len(a) > 1:
        l, r = a.popleft(), a.popleft()

        a.append(merge(l, r))

    a[0].sort()
    print(" ".join(str(p)for i, p in a[0]))
