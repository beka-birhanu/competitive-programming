n = int(input())
g = [[] for i in range(n)]

for j in range(n-1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

d = {1: set(), 0: set()}

st = [(0, 1)]
while st:
    curr, div = st.pop()
    d[div].add(curr)
    for nb in g[curr]:
        if nb not in d[1-div]:
            st.append((nb, 1-div))

ans = 0
for nod in d[1]:
    ans += (len(d[0])-len(g[nod]))

print(ans)
