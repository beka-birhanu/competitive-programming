# Problem: Previous Permutation With One Swap - https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        for i in range(N-2, -1, -1):
            if arr[i] > arr[i+1]:
                for j in range(N-1, i, -1):
                    if arr[i] > arr[j] and arr[j] != arr[j-1]:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                break
        
        return arr