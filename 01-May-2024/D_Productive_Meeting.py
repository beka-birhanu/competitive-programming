from heapq import heapify, heappop as pop, heappush as push


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = list((-ai, i+1) for i, ai in enumerate(a))
    heapify(a)

    ans = [0]
    while len(a) > 1:
        (ai, i), (aj, j) = pop(a), pop(a)
        if aj == 0:
            break

        ans[0] += 1
        ans.append((i, j))

        push(a, (aj + 1, j))
        push(a, (ai + 1, i))

    print(ans[0])
    for i, j in ans[1:]:
        print(i, j)
