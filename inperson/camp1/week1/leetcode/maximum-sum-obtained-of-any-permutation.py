class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0]*(len(nums)+1)

        for start,end in requests:
            arr[start] += 1
            arr[end+1] += -1
        
        for i in range(1,len(nums)):
            arr[i] += arr[i-1]
        arr.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(len(nums)):
            if not arr[i]:
                break
            ans += arr[i]*nums[i]

        return ans % (10**9 + 7)
        
