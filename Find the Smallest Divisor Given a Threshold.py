class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calculate(divisor):
            ans = 0
            for num in nums:
                ans += math.ceil(num/divisor)
  
            return ans

    
        l = math.ceil(sum(nums)/threshold)
        r = max(nums)

        while l < r:
            mid = l + (r-l)//2
            
            if calculate(mid) > threshold:
                l = mid + 1
            else:
                r = mid
        return r
