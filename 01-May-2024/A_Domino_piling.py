n, m = map(int, input().split())
print(max(n, m)//2 * min(n, m) + (max(n, m) % 2*min(n, m))//2)
