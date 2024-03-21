class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(i for i in nums if not i%2)
        answer = [0]*len(queries)
        for qi,(val,idx) in enumerate(queries):
            if not nums[idx]%2:
                even_sum -= nums[idx]

            nums[idx] += val
            if not nums[idx]%2:
                even_sum += nums[idx]
            
            answer[qi] = even_sum

        return answer