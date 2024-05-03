import bisect


n = int(input())
shops = sorted(map(int, input().split()))

for _ in range(int(input())):
    print(bisect.bisect(shops, int(input())))
