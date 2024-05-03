import sys
input = sys.stdin.readline


def dfs(nodes, curr, d):
    if nodes[curr][0] == 0 and nodes[curr][1] == 0:
        return 0

    left = len(d)
    right = len(d)
    if nodes[curr][0]:
        left = dfs(nodes, nodes[curr][0]-1, d)

    if nodes[curr][1]:
        right = dfs(nodes, nodes[curr][1]-1, d)

    if d[curr] == 0:
        right += 1

    elif d[curr] == 1:
        left += 1

    else:
        left += 1
        right += 1

    return min(left, right)


for _ in range(int(input())):
    n = int(input())
    d = list(input().strip())
    for i in range(n):
        if d[i] == "L":
            d[i] = 0

        elif d[i] == "R":
            d[i] = 1

        else:
            d[i] = -1

    nodes = [list(map(int, input().strip().split())) for j in range(n)]

    print(dfs(nodes, 0, d))


# for _ in range(int(input())):
#     n = int(input())
#     d = input()
#     nodes = [list(map(int, input().split())) for i in range(n)]

#     _min = float('inf')

#     st = [(0, 0)]
#     while st:
#         changes, curr = st.pop()
#         if max(nodes[curr]) == 0:
#             _min = min(_min, changes)
#             continue

#         left_changes = changes
#         right_changes = changes

#         if d[curr] != "R":
#             right_changes += 1

#         if d[curr] != "L":
#             left_changes += 1

#         if nodes[curr][0]:
#             st.append((left_changes, nodes[curr][0]-1))

#         if nodes[curr][1]:
#             st.append((right_changes, nodes[curr][1]-1))

#     print(_min)
