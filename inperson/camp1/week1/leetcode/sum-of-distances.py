class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        sum_freq = collections.defaultdict(lambda : [0,0]) # stores the [sum of indexes of that number, frequency of that number] in [:idx]
        arr = [0] * len(nums)

        #considering only the [:idx] part for the idx'th number
        for idx, num in enumerate(nums):
            idx_sum, freq = sum_freq[num]
            arr[idx] = (idx * freq) - idx_sum  #because (a-x) + (a-y) = (2*a) - (x+y)
            
            #update the idx_sum, freq
            sum_freq[num][0] += idx
            sum_freq[num][1] += 1
        
        sum_freq = collections.defaultdict(lambda : [0,0]) # stores the [sum of indexes of that number, frequency of that number] in [idx+1:]

        #considering only the [idx+1:] part for the idx'th number
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            idx_sum, freq = sum_freq[num]
            arr[idx] += idx_sum - (idx * freq)  #because (x-a) + (y-a) = (x+y) - (2*a)
            
            #update the idx_sum, freq
            sum_freq[num][0] += idx
            sum_freq[num][1] += 1

        return arr