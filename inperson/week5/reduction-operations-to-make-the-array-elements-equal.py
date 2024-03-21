class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        op = 0
        curr_smallest = nums[0]
        for i in range(len(nums)):
            if nums[i] == curr_smallest:
                continue
            
            op += len(nums)-i
            curr_smallest = nums[i]
            
        return op