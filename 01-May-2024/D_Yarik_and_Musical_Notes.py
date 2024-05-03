for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (max(max(a)+1, 3))  # Adjust the size based on your constraints
    for x in a:
        ans += cnt[x]
        if x == 1:
            ans += cnt[2]
        elif x == 2:
            ans += cnt[1]
        cnt[x] += 1
    print(ans)
