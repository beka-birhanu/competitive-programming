# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

n = int(input())
x = sorted(map(int, input().split()))
q = int(input())
m = sorted((int(input()), idx) for idx in range(q))
ans = [0]*q
j = 0
for i in range(q):
    while j < len(x) and m[i][0] >= x[j]:
        j += 1
    ans[m[i][1]] = j
for i in range(q):
    print(ans[i])
