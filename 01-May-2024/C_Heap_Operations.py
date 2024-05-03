from heapq import heapify, heappop as pop, heappush as push

n = int(input())
heap = []
ops = []
for _ in range(n):
    log = input().split()
    if len(log) == 2:
        op, val = log
        val = int(val)
        if op == "insert":
            push(heap, val)

        else:

            while heap and heap[0] < val:
                pop(heap)
                ops.append('removeMin')

            while not heap or heap[0] > val:
                push(heap, val)
                ops.append(f"insert {val}")
    else:
        if heap:
            pop(heap)
        else:
            ops.append(f"insert 5")

    ops.append(" ".join(log))

print(len(ops))
for op in ops:
    print(op)
