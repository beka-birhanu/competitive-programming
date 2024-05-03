from typing import List


def merge(left, right) -> List[int]:
    merged_arr = []
    left.append(float('inf'))
    right.append(float('inf'))

    p1, p2 = 0, 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            merged_arr.append(left[p1])
            p1 += 1
        else:
            merged_arr.append(right[p2])
            p2 += 1

    merged_arr.pop()

    return merged_arr


def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]

    mid = (left+right)//2
    left = mergeSort(left, mid, arr)
    right = mergeSort(mid+1, right, arr)

    return merge(left, right)


def test():

    print(mergeSort(0, 5, [3, 0, 2, -5, 10, 2]))
    print(mergeSort(0, 2, [1, 2, 3]))
    print(mergeSort(0, 2, [3, 2, 1]))
    print("Great Job !!!")


test()

