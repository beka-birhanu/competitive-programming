for _ in range(int(input())):
    a, b, l = map(int, input().split())
    ans = set()

    for x in range(21):
        for y in range(21):
            k = l/((a**x)*(b**y))
            if k == int(k):
                ans.add(k)

    print(len(ans))
