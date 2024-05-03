v, e = map(int, input().split())
g = [[] for _ in range(v)]
for i in range(e):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

one = 0
for i in range(v):
    if len(g[i]) == 1:
        one += 1

two = 0
for i in range(v):
    if len(g[i]) == 2:
        two += 1


if one == v-1:
    print("star topology")

elif one == 2 and two == v-2:
    print("bus topology")

elif two == v:
    print("ring topology")

else:
    print("unknown topology")
