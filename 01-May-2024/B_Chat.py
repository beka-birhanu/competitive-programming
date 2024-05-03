from heapq import heappop as pop, heappush as push
n, k, q = map(int, input().split())
f = list(map(int, input().split()))
top_k = []

for _ in range(q):
    typ, id = map(int, input().split())
    if typ == 1:
        push(top_k, f[id-1])

        if len(top_k) > k:
            pop(top_k)

    elif f[id-1] in top_k:
        print("YES")

    else:
        print("NO")
