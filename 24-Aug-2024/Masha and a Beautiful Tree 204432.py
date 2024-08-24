# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def mergeSortAndCount(nums):
    N = len(nums)
    if N <= 1:
        return nums, 0

    left_list, left_count = mergeSortAndCount(nums[:N//2])
    if left_count == -1:
        return [], -1

    right_list, right_count = mergeSortAndCount(nums[N//2:])
    if right_count == -1:
        return [], -1

    merged_list,  count = mergeAndCount(left_list, right_list)
    if count == -1:
        return [], -1

    return merged_list, sum((left_count, right_count, count))


def mergeAndCount(left, right):
    count = 0
    if not (left or right):
        return left+right, count

    if (left[0], left[-1]) > (right[0], right[-1]):
        left, right = right, left
        count = 1

    if left[-1] > right[0]:
        return [], -1
    else:
        return left+right, count


for _ in range(int(input())):
    n = int(input())
    m = list(map(int, input().split()))
    _, count = mergeSortAndCount(m)
    print(count)
