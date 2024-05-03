from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = defaultdict(int)

    digit = []
    for num in a:
        num %= 10
        if count[num] < 3:
            digit.append(num)
            count[num] += 1

    digit.sort()
    ans = "NO"
    for i in range(len(digit)):
        if ans == "YES":
            break
        for j in range(i+1, len(digit)):
            if ans == "YES":
                break
            for k in range(j+1, len(digit)):
                if (digit[i]+digit[j]+digit[k]) % 10 == 3:
                    ans = "YES"
                    break

    print(ans)
