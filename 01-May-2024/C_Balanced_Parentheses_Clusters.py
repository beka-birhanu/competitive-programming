def find(parents, i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]

    return i


for _ in range(int(input())):
    n = int(input())
    s = input()
    p = [i for i in range(len(s))]

    st = []
    for i, b in enumerate(s):
        if b == ")":
            j = st.pop()
            p_j = find(p, j)
            p_i = find(p, i)

            p[p_i] = p_j
            if len(st) == 0:
                p[find(p, j)] = find(p, 0)

            else:
                p[find(p, j)] = p[find(p, st[-1]+1)]

        else:
            st.append(i)
    print(len(set(find(p, i) for i in range(len(s)))))
