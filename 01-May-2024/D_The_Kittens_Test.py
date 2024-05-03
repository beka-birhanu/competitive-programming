def find(parents, i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]

    return i


class node:
    def __init__(self, val) -> None:
        self.val = val
        self.n = None


n = int(input())
g = {}
for i in range(n):
    no = node(str(i+1))
    g[i] = [no, no]

p = [i for i in range(n)]
count = [1] * n

for _ in range(n-1):
    i, j = map(int, input().strip().split())
    p_i = find(p, i-1)
    p_j = find(p, j-1)
    if p_i == p_j:
        continue

    p[p_i] = p_j
    g[p_j][1].n = g[p_i][0]
    g[p_j][1] = (g[p_i][1])
    count[p_j] += count[p_i]

for i in range(n):
    if count[i] == n:
        ans = []
        cur = g[i][0]
        while cur:
            ans.append(cur.val)
            cur = cur.n

        print(" ".join(ans))
        break
