q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]
    used = [0] * n
    ans = [0] * n
    for j in range(n):
        if not used[j]:
            cur = []
            while not used[j]:
                cur.append(j)
                used[j] = 1
                j = p[j]
            for el in cur:
                ans[el] = len(cur)
    print(*ans)
