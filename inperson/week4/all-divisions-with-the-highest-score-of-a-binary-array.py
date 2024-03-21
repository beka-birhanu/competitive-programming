class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cur_max = 0
        scores = [0]*n
        max_scores = set()
        left = 0
        right = 0

        for i in range(len(nums)):
            scores[i], left = scores[i]+i-left, left+nums[i]
            right += nums[n-i-1]
            scores[n-i-1] += right
            if scores[i] > scores[n-i-1]:
                if scores[i] > cur_max:
                    cur_max = scores[i]
                    max_scores = set([i])
                elif scores[i] == cur_max:
                    max_scores.add(i)
            elif scores[i] < scores[n-i-1]:
                if scores[n-i-1] > cur_max:
                    cur_max = scores[n-i-1]
                    max_scores = set([n-i-1])
                elif scores[n-i-1] == cur_max:
                    max_scores.add(n-i-1)
            else:
                 if scores[n-i-1] > cur_max:
                    cur_max = scores[n-i-1]
                    max_scores = set([n-i-1,i])
        
        if  n-left > cur_max:
            max_scores = set([n])
        elif n-left == cur_max:
            max_scores.add(n)
                    
            
        return max_scores
        
        