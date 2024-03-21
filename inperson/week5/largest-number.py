class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        
        for i in range(len(nums)):
            swapped = False
            
            for j in range(len(nums)-i-1):
                if nums[j]+nums[j+1] < nums[j+1]+nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        for num in nums:
            if num != "0":
                return ("".join(nums))
        return "0"