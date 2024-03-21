class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        triangle_count = 0

        for k in range(len(nums)-1,1,-1):
            i, j = 0, k-1
            while i < j:
                if 2*nums[j] < nums[k]:
                    break
                
                if nums[i] + nums[j] > nums[k]:
                    
                    triangle_count += j-i
                    j -= 1
                else:
                    i += 1
                    
        return triangle_count