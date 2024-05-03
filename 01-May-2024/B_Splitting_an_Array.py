import heapq


def possible(max_sum, a, k):
    pref = 0
    parts = 1
    for num in a:

        pref += num
        if pref > max_sum:
            pref = num
            parts += 1

            if parts > k:
                return False

    return True


n, k = map(int, input().split())
a = list(map(int, input().split()))

_min = max(a)
_max = sum(a)
while _min < _max:
    mid = (_min + _max)//2
    if possible(mid, a, k):
        _max = mid

    else:
        _min = mid + 1
print(_max)
