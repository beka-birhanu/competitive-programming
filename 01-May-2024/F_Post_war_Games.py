from sys import stdin


def input(): return stdin.readline().strip()


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    if N == K:
        print(0)
        continue

    ans = (N - (K + 1))*3 + ((K - 1)//2)*3 + (K - 1) % 2 + 1
    print(ans)
