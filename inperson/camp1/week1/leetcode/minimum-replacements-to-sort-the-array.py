class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                ops += math.ceil(nums[i]/nums[i+1])-1
                nums[i] //= math.ceil(nums[i]/nums[i+1])
        return ops
