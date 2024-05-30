# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sum_freq = collections.defaultdict(lambda : [0,0])
        arr = [0] * len(nums)

        #considering only the [:idx] part for the idx'th number
        for idx, num in enumerate(nums):
            idx_sum, freq = sum_freq[num]
            arr[idx] = (idx * freq) - idx_sum  #because (a-x) + (a-y) = (2*a) - (x+y)
            
            sum_freq[num][0] += idx
            sum_freq[num][1] += 1
        
        sum_freq = collections.defaultdict(lambda : [0,0]) 

        #considering only the [idx+1:] part for the idx'th number
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            idx_sum, freq = sum_freq[num]
            arr[idx] += idx_sum - (idx * freq)  #because (x-a) + (y-a) = (x+y) - (2*a)
            
            sum_freq[num][0] += idx
            sum_freq[num][1] += 1

        return arr