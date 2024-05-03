for _ in range(int(input())):
    n, m = map(int, input().split())
    g = []
    for i in range(n):
        g.append(list(input()))

    gs = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == "G":
                gs += 1

    for i in range(n):
        for j in range(m):
            if g[i][j] == "B":

                x, y = i, j
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != "B":
                        g[nx][ny] = "#"
    another = set()
    for i in range(n):
        for j in range(m):
            if g[i][j] == "G":
                if (i, j) in another:
                    gs -= 1
                    continue
                st = [(i, j)]
                visited = set([(i, j)])
                pos = 0
                while st:
                    x, y = st.pop()
                    if x == n-1 and y == m-1:
                        pos = 1
                        break

                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and (nx, ny)not in visited:
                            if g[nx][ny] != "#":
                                st.append((nx, ny))
                                visited.add((nx, ny))
                if pos:
                    another = another | visited
                    gs -= 1

    if gs == 0:
        print("Yes")

    else:
        print("No")
