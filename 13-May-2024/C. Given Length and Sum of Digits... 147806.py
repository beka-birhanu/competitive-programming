# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

def can(m, s):
    return 0 <= s <= 9 * m


def find_min_number(m, s):
    _min = ""
    for i in range(m):
        for d in range(10):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, s - d):
                _min += str(d)
                s -= d
                break

    if not _min or len(str(int(_min))) < len(_min) or s > 0 or len(_min) != m:
        return '-1'

    else:
        return _min if _min else '-1'


def find_max_number(m, s):
    _max = ""
    for i in range(m):
        for d in range(9, -1, -1):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, s - d):
                _max += str(d)
                s -= d
                break

    if not _max or len(str(int(_max))) < len(_max) or s > 0 or len(_max) != m:
        return '-1'

    else:
        return _max


m, s = map(int, input().split())
_min = find_min_number(m, s)
_max = find_max_number(m, s)
print(_min, _max)
