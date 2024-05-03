for _ in range(int(input())):
    n, k = map(int, input().split())
    blancket = 0
    for j in range(n):
        blancket += max(map(int, input().split()))

    if blancket >= k:
        print("YES")
    else:
        print("NO")
