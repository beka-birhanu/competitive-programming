t = int(input())
while t > 0:
    a, b = map(int,input().split())
    print(min(a, b, (a + b) // 4))
    t -= 1
