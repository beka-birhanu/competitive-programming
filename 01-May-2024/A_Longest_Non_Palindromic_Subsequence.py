from typing import Counter


for _ in range(int(input())):
    s = input()
    c = Counter(s)

    if len(c) == 1:
        print(-1)
        continue

    else:
        print(len(s)-1)
