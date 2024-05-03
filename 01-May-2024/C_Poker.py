from heapq import heappop as pop, heappush as push

for _ in range(int(input())):
    n = int(input())
    d = map(int, input().split())
    power = 0
    hp = []
    for dval in d:
        if dval > 0:
            push(hp, -dval)

        elif hp:
            power += -pop(hp)

    print(power)
