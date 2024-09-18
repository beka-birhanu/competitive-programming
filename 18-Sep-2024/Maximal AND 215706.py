# Problem: Maximal AND - https://codeforces.com/problemset/problem/1669/H

for _ in range(int(input())):
    count = [0]*31
    n, k = map(int, input().split())
    for num in map(int, input().split()):
        idx = 0
        while num > 0:
            if num & 1:
                count[idx] += 1
            num >>= 1
            idx += 1

    ans = 0
    for i in range(30, -1, -1):
        ans <<= 1
        if n-count[i] <= k:
            k -= (n-count[i])
            count[i] = n
        if count[i] == n:
            ans |= 1
    print(ans)
