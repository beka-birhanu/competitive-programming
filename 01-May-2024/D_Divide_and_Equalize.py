from collections import defaultdict
import math


def add_prime_factors(x, prime_factors):
    i = 2
    while i * i <= x:
        while x % i == 0:
            prime_factors[i] += 1
            x //= i

        i += 1

    if x > 1:
        prime_factors[x] += 1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prime_factors = defaultdict(int)

    for num in a:
        add_prime_factors(num, prime_factors)

    for freq in prime_factors.values():
        if freq % n != 0:
            print("NO")
            break

    else:
        print("YES")
