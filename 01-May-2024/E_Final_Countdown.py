# import sys
# for _ in range(int(input())):
#     p = 0
#     total_time = 0

#     digits = int(input())
#     n = input()

#     for i in range(digits):
#         curr = int(n[-i-1])

#         # print(p, time(i))
#         total_time += curr * p + curr
#         p = p*10 + 10
#         # print(curr, i)

#     print(total_time)


# Author: pashka


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()[::-1]
    a = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        a[i] = a[i + 1] + int(s[i])

    res = []
    c = 0
    for i in range(n):
        c += a[i]
        res.append(str(c % 10))
        print(res, c)
        c //= 10

    res += str(c)
    while res[-1] == '0':
        res.pop()
    print("".join(res[::-1]))
