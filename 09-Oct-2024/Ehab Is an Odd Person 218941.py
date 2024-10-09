# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

from heapq import heappush

n = int(input())
nums = input().split()
odds = []
evens = []
i = n-1
while i >= 0:
    if int(nums[i]) % 2 == 0:
        heappush(evens, (nums[i], i))
        if odds and odds[0][0] < nums[i]:
            num, idx = odds[0]
            nums[idx] = nums[i]
            nums[i] = num
            i += 1
    else:
        heappush(odds, (nums[i], i))
        if evens and evens[0][0] < nums[i]:
            num, idx = evens[0]
            nums[idx] = nums[i]
            nums[i] = num
            i += 1
    i -= 1
print(" ".join(nums))
