def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = (len(arr))//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    arr = merge(left, right)

    return arr


def merge(left, right):
    merged_arr = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1

    while l < len(left):
        merged_arr.append(left[l])
        l += 1

    while r < len(right):
        merged_arr.append(right[r])
        r += 1

    return merged_arr


print(merge_sort([9, 19, 51945, 13, 3, 1, 4, 51, 324059, 34, 1, 423, 51]))
