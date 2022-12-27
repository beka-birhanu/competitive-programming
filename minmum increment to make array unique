class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        k = 0
        counter = Counter(nums)
        max_ = max(nums)
        duplicates = []
        for i in range(len(nums) + max_):
            if counter[i] > 1:
                duplicates.extend([i]*(counter[i]-1))
            elif not counter[i] and duplicates:
                k += (i-duplicates.pop())
        return k
        
        
        
        
        
        
        
        
        
#class Solution:
#   def minIncrementForUnique(self, nums: List[int]) -> int:
#        k = 0
#       counter = Counter(nums)
#        for i in range(len(nums)):
#           while counter[nums[i]] > 1:
#               counter[nums[i]] -=1
#               k+=counter[nums[i]]
#               nums[i]+=counter[nums[i]]
#               counter[nums[i]] +=1
#        return k 
