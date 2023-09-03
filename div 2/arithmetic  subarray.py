class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checker(arr):
            n = len(arr)
            if n >=2:
                arr.sort()
                d =arr[0] - arr[1]
                for i in range(1,n-1):
                    if arr[i] - arr[i+1] != d:
                        return False
                return True
            else:
                return False

        def subArr(i, l, r, nums):
            return nums[l[i]: r[i] + 1]

        ans = []
        for i in range(len(l)):
            ans.append(checker(subArr(i,l,r,nums)))
        return ans
