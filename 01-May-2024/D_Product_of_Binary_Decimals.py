b = [10, 11, 110, 100, 101, 111, 1110, 1010,
     1100, 1000, 1101, 1101, 1001, 1111, 10111]


def backtrack(mult, t):
    if mult > t:
        return False
    if mult == t:
        return True
    for i in range(14):
        mult *= b[i]
        if mult == t:
            return True
        if backtrack(mult, t):
            return True
        mult //= b[i]

    return False


for _ in range(int(input())):
    n = input()
    if int(max(n)) <= 1:
        print("YES")

    elif backtrack(1, int(n)):
        print("YES")

    else:
        print("NO")
