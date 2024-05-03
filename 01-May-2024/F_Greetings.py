def merge_sort(arr, dic):

    if len(arr) <= 1:
        return 0, arr

    mid = (len(arr))//2
    meet1, left = merge_sort(arr[:mid], dic)
    meet2, right = merge_sort(arr[mid:], dic)

    meet3, arr = merge(left, right, dic)

    return sum((meet2, meet1, meet3)), arr


def merge(left, right, dic):
    merged_arr = []
    meets = 0
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if dic[left[l]] < dic[right[r]]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
            meets += len(left)-l
    while l < len(left):
        merged_arr.append(left[l])
        l += 1
    while r < len(right):
        merged_arr.append(right[r])
        r += 1

    return meets, merged_arr


for _ in range(int(input())):
    n = int(input())
    starts = []
    dic = {}
    for i in range(n):
        s, e = map(int, input().split())
        starts.append(s)
        dic[s] = e
    starts.sort()
    print(merge_sort(starts, dic)[0])
