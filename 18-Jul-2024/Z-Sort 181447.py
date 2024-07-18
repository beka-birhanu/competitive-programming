# Problem: Z-Sort - https://codeforces.com/problemset/problem/652/B

n = input()
A = list(map(int, input().split()))

for i in range(len(A) - 1):
    A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)

print(*A)