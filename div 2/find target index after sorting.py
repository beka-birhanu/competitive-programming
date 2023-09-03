class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for idx in range(len(nums)):
            if nums[idx] == target:
                result.append(idx)
        return result
