import math


n = int(input())
walls = list(map(int, input().split()))

shot = float("inf")
for i in range(1, n-1):
    x, y = walls[i-1], walls[i+1]
    shot = min(math.ceil((x+y)/2), shot)

for i in range(n-1):
    x, y = walls[i], walls[i+1]
    shot = min(max(math.ceil(max(x, y)/2), math.ceil((x+y)/3)), shot)


walls.sort()
x, y = walls[0], walls[1]

print(min(shot, math.ceil(x/2)+math.ceil(y/2)))
