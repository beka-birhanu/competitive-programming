# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def union(x, y):
    y = find(y)
    x = find(x)
    parent[x] = parent[y]


n, q = map(int, input().split())
parent = [i for i in range(n)]
range_connection = [i+1 for i in range(n)]

for _ in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1

    if t == 1:
        union(x, y)

    elif t == 2:
        union(x, y)
        target = range_connection[y]
        person = x
        while person < target:
            union(person, x)
            next_person = range_connection[person]
            range_connection[person] = target
            person = next_person
    else:
        p_x, p_y = find(x), find(y)
        if p_x == p_y:
            print('YES')
        else:
            print('NO')
