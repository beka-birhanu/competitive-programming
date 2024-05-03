import math


for _ in range(int(input())):
    x = int(input())
    if x == 1:
        print(3)
        continue
    lg = math.log2(x)
    if lg == lg//1:
        print(x + 1)
        continue

    p = bin(x)[:1:-1].find('1')

    print(2**p)
