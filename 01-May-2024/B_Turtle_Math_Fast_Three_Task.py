from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    # print(tot, "t")
    if tot % 3 == 1:
        rem = Counter(map(lambda x: x % 3, a))
        if rem[1]:
            print(1)
        else:
            print(2)
    elif tot % 3 == 2:

        print(1)

    else:
        print(0)
