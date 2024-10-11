# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

s = input().strip()
n = len(s)
t = []
u = []

min_chars = [None] * n
min_chars[-1] = s[-1]

for i in range(n - 2, -1, -1):
    min_chars[i] = min(s[i], min_chars[i + 1])

i = 0
while i < n or t:
    while t and (i == n or t[-1] <= min_chars[i]):
        u.append(t.pop())
    if i < n:
        t.append(s[i])
        i += 1

print("".join(u))
