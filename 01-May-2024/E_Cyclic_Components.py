import sys


input = sys.stdin.readline
N = 200011

n, m = map(int, input().split())
used = [False] * N
comp = []
g = [[] for _ in range(N)]


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)


ans = 0
for i in range(n):
    if not used[i]:
        comp = []
        st = [i]
        ok = True
        while st:
            v = st.pop()
            used[v] = True

            if len(g[v]) != 2:
                ok = False

            for to in g[v]:
                if not used[to]:
                    st.append(to)

        if ok:
            ans += 1

print(ans)
