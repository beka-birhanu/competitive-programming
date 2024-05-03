for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + a[i - 1]

    q = int(input())
    for _ in range(q):
        l, u = map(int, input().split())
        lb, rb = l, n
        while lb < rb:
            mid = (lb + rb + 1) // 2

            if ps[mid] - ps[l - 1] <= u:
                lb = mid
            else:
                rb = mid - 1

        maxu, optid = -float('inf'), None
        for i in range(max(l, lb - 2), min(n, lb + 2) + 1):
            t = ps[i] - ps[l - 1]

            ut = (u + (u - t + 1)) * t // 2
            if ut > maxu:
                maxu = ut
                optid = i

        print(optid, end=" ")

    print()
