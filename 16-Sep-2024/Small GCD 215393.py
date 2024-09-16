# Problem: Small GCD - https://codeforces.com/contest/1900/problem/D

from collections import Counter


def getFactors(num):
    factors = {1, num}
    i = 2
    while i * i <= num:
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
        i += 1
    return factors


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    counts = Counter()
    GCD_count = Counter()
    for i in range(n):
        for fact in getFactors(arr[i]):
            GCD_count[fact] += counts[fact] * (n - i - 1)
            counts[fact] += 1

    keys = list(GCD_count.keys())
    keys.sort(reverse=True)

    for num in keys:
        prevs = getFactors(num)
        prevs.remove(num)

        for prev in prevs:
            GCD_count[prev] -= GCD_count[num]

    total = 0
    for num in keys:
        total += num * GCD_count[num]

    print(total)