for _ in range(int(input())):
    n = int(input())
    ans = [["#"]*2*n for i in range(2*n)]
    for i in range(2*n):
        for j in range(2*n):
            if ((i//2) % 2 or (j//2) % 2) and not ((i//2) % 2 and (j//2) % 2):
                ans[i][j] = "."

        print("".join(ans[i]))
