class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = inf
        for i in range(len(nums)-2):
            k = i+1
            j = len(nums)-1
            sum_left = target-nums[i]
            while k < j:
                cur_sum = nums[k] + nums[j]
                closest_sum = min(-sum_left+cur_sum+target, closest_sum, key = lambda x:abs(x-target))

                if cur_sum > sum_left:
                    j -= 1

                elif cur_sum < sum_left:
                    k += 1
                
                else:
                    return target
                
        return closest_sum