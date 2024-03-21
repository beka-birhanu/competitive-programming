class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_to_modifie = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if i < len(nums)-2 and nums[i]<nums[i+2]:
                    pass
                elif i > 0 and nums[i-1] > nums[i+1]:
                    if i < len(nums)-2:
                        return False
                num_to_modifie += 1
            
            if num_to_modifie > 1:
                return False
        return True