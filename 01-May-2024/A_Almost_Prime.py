def is_almost(n):
    factors = set()
    d = 2

    while d ** 2 <= n:
        if not n % d:
            factors.add(d)

        while not n % d:
            n //= d

        d += 1
        if len(factors) > 2:
            return False
    if n > 1:
        factors.add(n)
    return len(factors) == 2


n = int(input())
count = 0

for i in range(6, n+1):
    if is_almost(i):
        count += 1

print(count)
