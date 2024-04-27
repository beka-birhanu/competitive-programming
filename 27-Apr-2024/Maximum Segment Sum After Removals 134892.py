# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        def find(parents, i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]
                i = parents[i]

            return i
        
        n = len(nums)
        parents = [i for i in range(n)]
        group_sum = [num for num in nums]

        ans = [0]*n
        seen = set()
        max_sum = 0

        for i in range(n-1, -1, -1):
            idx = removeQueries[i]
            if idx > 0 and idx -1 in seen:
                left_group = find(parents, idx-1)
                parents[left_group] = idx
                group_sum[idx] += group_sum[left_group]
            
            if idx < n-1 and idx+1 in seen:
                right_group = find(parents, idx+1)
                parents[right_group] = idx
                group_sum[idx] += group_sum[right_group] 
            
            ans[i] = max_sum
            seen.add(idx)
            max_sum = max(max_sum, group_sum[idx])
        
        return ans
            



