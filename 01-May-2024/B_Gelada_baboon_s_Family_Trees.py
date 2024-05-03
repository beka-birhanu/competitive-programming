def find(parents, i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]

    return i


n = int(input())
a = list(map(int, input().strip().split()))

p = [i for i in range(n)]

for i, nu in enumerate(a):
    p_i = find(p, i)
    p_nu = find(p, nu-1)
    p[p_i] = p_nu

print(len(set(find(p, i) for i in range(n))))
