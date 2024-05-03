import math


def is_one(pos, target, num):
    if num < 2:
        return num
    if pos + 1 == 2 * target:
        return num % 2
    num //= 2
    pos //= 2
    if target > pos + 1:
        target -= (pos + 1)
    return is_one(pos, target, num)


n, l, r = map(int, input().split())
x = 2 ** int(math.log2(max(n, 1))+1) - 1
ans = 0
for i in range(l, r + 1):
    ans += is_one(x, i, n)
print(ans)
