class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j, k = i+1, len(nums)-1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if cur_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < len(nums)-1 and nums[j] == nums[j+1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                    j += 1
                elif cur_sum < 0:
                    
                    j += 1
                else:
                    k -= 1
        return ans 