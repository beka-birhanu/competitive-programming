import bisect


n, k, a, b = map(int, input().split())
av = sorted(map(int, input().split()))


def burn(avengers, l, r, a, b):

    if len(avengers) == 0:
        return a

    if r - l == 0:
        return b * len(avengers)

    mid = bisect.bisect_right(avengers, (l+r)//2)
    return min(b * len(avengers) * (r-l+1), burn(avengers[:mid], l, (l+r)//2, a, b) + burn(avengers[mid:], (l+r)//2+1, r, a, b))


print(burn(av, 1, 2**n, a, b))
