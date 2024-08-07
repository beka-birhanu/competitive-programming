# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

def find(parents, i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]

    return i

n, m, k = map(int, input().split())
parents = [i for i in range(n)]

for _ in range(m):
    input()

qs = []
for _ in range(k):
    qs.append(input().split())

ans = []
for i in range(k-1, -1, -1):
    q, x, y = qs[i]
    x = int(x)-1
    y = int(y)-1
    if q == "ask":
        if find(parents, x) == find(parents, y):
            ans.append("YES")

        else:
            ans.append("NO")

    else:
        px = find(parents, x)
        py = find(parents, y)

        parents[px] = py

for i in range(len(ans)-1, -1, -1):
    print(ans[i])
