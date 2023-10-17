# Runtime 343ms and Memory 16.29MB
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n,res=len(nums),[]

        for i in range(0,n-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            if target-nums[i] < nums[i+1]*3:
                break 
            j = i + 1
            while j < n-2:
                t = target - nums[i] - nums[j]
                if t < nums[j+1]*2:
                    break 
                l, r = j+1, n-1
                while l < r:
                    if nums[l]+nums[r] == t:                     
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        temp_l = nums[l]
                        temp_r = nums[r]
                        while(l<r and nums[l]==temp_l):
                            l+=1
                        while(l<r and nums[r]==temp_r):
                            r-=1
                    elif nums[l]+nums[r] < t:
                        l += 1
                    else:
                        r -= 1
                while j < n-2 and nums[j] == nums[j+1]:
                    j += 1
                j += 1 
        return res
