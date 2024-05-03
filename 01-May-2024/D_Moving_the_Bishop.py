from collections import deque


n = int(input())
ai, aj = map(int, input().split())
bi, bj = map(int, input().split())

g = []
for _ in range(n):
    row = input()
    g.append(row)

q = deque([(ai-1, aj-1)])
d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
visited = {1: set(), -1: set()}
moves = 0


while q:
    for _ in range(len(q)):
        i, j = q.popleft()

        if i == bi-1 and bj-1 == j:
            print(moves)
            exit()

        for di, dj in d:
            ni, nj = i+di, j+dj
            while 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited[di*dj] and g[ni][nj] != "#":
                q.append((ni, nj))
                visited[di*dj].add((ni, nj))
                ni += di
                nj += dj
                # break

    moves += 1

print(-1)
