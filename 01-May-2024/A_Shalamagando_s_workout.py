n = int(input())
a = list(map(int, input().split()))

d = {1: 0, 2: 0, 0: 0}
for i, ai in enumerate(a):
    d[i % 3] += ai

m = max(d, key=lambda x: d[x])

if m == 0:
    print('chest')
elif m == 1:
    print('biceps')

else:
    print('back')
