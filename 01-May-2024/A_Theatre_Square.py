import math


n, m, a = map(int, input().split())
print(math.ceil((m)/a) * math.ceil(n/a))
