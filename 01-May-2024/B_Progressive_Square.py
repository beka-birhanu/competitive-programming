from collections import Counter


def solve():
    n, c, d = map(int, input().split())
    nums = Counter(map(int, input().split()))
    a11 = min(nums)
    header = []
    for i in range(n):
        if a11 in nums:
            header.append(a11)
            a11 += d
        else:
            print("NO")
            return

    for h in header:
        for i in range(n):
            if h not in nums:
                print("NO")
                return
            nums[h] -= 1
            if nums[h] == 0:
                nums.pop(h)
            h += c

    print("YES")


for t in range(int(input())):
    solve()
