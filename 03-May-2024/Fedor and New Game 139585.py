# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())
p = []
for _ in range(m):
    p.append(int(input()))

f = int(input())
f_c = 0

while p:
    if bin(f^p.pop())[2:].count("1") <= k:
        f_c += 1
print(f_c)