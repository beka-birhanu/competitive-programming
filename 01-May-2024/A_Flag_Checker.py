n, m = map(int, input().split())
prev = -1
for _ in range(n):
    row = list(map(int, list(input())))
    if max(row) != min(row):
        print("NO")
        exit()

    if max(row) == prev:
        print("NO")
        exit()

    prev = max(row)

print("YES")
