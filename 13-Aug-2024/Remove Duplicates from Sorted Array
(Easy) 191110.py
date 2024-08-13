# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 
        for j in range(1,len(nums)):
            if nums[k] == nums[j]:
                continue
            k += 1
            nums[k], nums[j] = nums[j], nums[k]
            
        return k+1