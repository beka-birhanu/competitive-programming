def find_position(l, r, positions, curr_depth):
    if l > r:
        return None

    _max_idx = l
    for i in range(l, r+1):
        _max_idx = max(i, _max_idx, key=lambda x: positions[x])

    positions[_max_idx] = str(curr_depth)

    find_position(l, _max_idx-1, positions, curr_depth+1)
    find_position(_max_idx+1, r, positions, curr_depth+1)


for _ in range(int(input())):
    n = int(input())
    positions = list(map(int, input().split()))

    find_position(0, n-1, positions, 0)

    print(" ".join(positions))
