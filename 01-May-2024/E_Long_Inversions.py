import math


def possible(k, s):
    si = list(map(int, s))
    # print(len(s)-k, "k")
    for i in range(min(len(s)-k+1, len(s))):
        # print(i, k)
        if si[i] == 1:
            # print(i, "j")
            continue
        else:
            for j in range(i, i+k):
                si[j] = abs(1-si[j])
                print(si, i)
    return si.count(0) == 0


for _ in range(int(input())):
    n = int(input())
    s = input()
    l = 0
    r = n
    while l < r:
        m = math.ceil((l+r)/2)
        print(m)
        if possible(m, s):
            l = m
        else:
            r = m-1

    print(l)
