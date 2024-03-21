class Solution:
    def maxScore(self, s: str) -> int:
        scores = [0] * len(s)
        zeroes = 0
        ones = int(s[-1])
        max_score = 0

        for i in range(len(s)-1):

            zeroes += abs(int(s[i])-1)
            scores[i] += zeroes

            scores[len(s)-i-2] += ones
            ones += int(s[len(s)-i-2])
            
            max_score = max(max_score, scores[i], scores[len(s)-i-2])

        return max_score