for _ in range(int(input())):
    n, k = map(int, input().split())
    k = str(k)
    a = list(input())
    for i in range(n):
        if a[i] < k:
            a.insert(i, k)
            break

    if len(a) > n:
        print("".join(a))

    else:
        print("".join(a)+k)
