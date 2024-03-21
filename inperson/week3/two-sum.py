class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # stores numbers maped to their index
        dic = {num:idx for idx,num in enumerate(nums)}
        
        for i in range(len(nums)):
            if target - nums[i]  in dic and dic[target-nums[i]] != i:
                return [i,dic[target-nums[i]]]
