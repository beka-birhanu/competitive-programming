T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    s = list(map(ord, input()))
    w = sum(map(ord, input()))
    s.append(0)

    for i in range(1, n-1):
        s[i] += s[i-1]
    print(s)

    for i in range(n-1, m):
        s[i] += s[i-1]
        if s[i] - s[i-n] == w:
            print('YES')
            break

    else:
        print('NO')
