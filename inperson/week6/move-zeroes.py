class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 # end of non zero portion
        
        # iterate to find zeroes
        for j in range(len(nums)):
            # if non-zero number found swap with the first zero and increment i
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            
        