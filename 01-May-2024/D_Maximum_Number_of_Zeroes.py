import math
import sys
from collections import defaultdict
from random import getrandbits

RANDOM = getrandbits(32)


class Wrapper(int):
    def __new__(cls, x):
        return super().__new__(cls, x)

    def __hash__(self):
        return super().__hash__() ^ RANDOM


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(int)
any = 0

for i in range(n):
    if a[i] != 0 and b[i] != 0:
        g = math.gcd(b[i], a[i])
        d[(abs(b[i]) // g, abs(a[i])//g, b[i]*a[i] > 0)] += 1
    if b[i] == 0:
        if a[i] != 0:
            d[0] += 1
        else:
            any += 1

a = d.values()
if a:
    print(max(a)+any)
else:
    print(any)
