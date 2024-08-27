# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)

st = [0]
while st:
    cur = st.pop()
    if cur == t - 1:
        print("YES")
        break

    if a[cur] != 0:
        st.append(cur + a[cur])
        a[cur] = 0

else:
    print("NO")
