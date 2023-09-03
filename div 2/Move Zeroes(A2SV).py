class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        #i while hold the firs occuruns of 0
        i = -1 
        for k in range(n):
            if nums[k] == 0:
                i = k
                break
        #if no zero in nums no work needed
        if i == -1:
            return
        
        for j in range(i,n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
