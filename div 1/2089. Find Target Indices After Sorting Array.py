class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def check_left(m)-> None:
            nonlocal ans
            while m>=0 and nums[m] == target:
                ans = [m] + ans
                m -= 1

        def check_right(m):
            nonlocal ans
            while m < len(nums) and nums[m] == target:
                ans =  ans + [m]
                m += 1
        nums.sort()
        ans = []
        l,r = 0,len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                check_left(m-1)
                ans.append(m)
                check_right(m+1)
                return ans
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return  []
