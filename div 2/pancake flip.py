class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        ans = []
        for i in range(len(arr)-1,0,-1):
            sub_arr = arr[:i]
            sub_arr_maxIndex = arr.index(max(sub_arr))
            if arr[i] < arr[sub_arr_maxIndex]:
                reverse(sub_arr_maxIndex)
                reverse(i)
                ans.append(sub_arr_maxIndex+1)
                ans.append(i+1)
        return ans
