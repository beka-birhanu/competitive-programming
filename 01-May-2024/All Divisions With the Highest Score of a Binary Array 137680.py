# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_score = 0
        right_score = nums.count(1)
        max_score = left_score + right_score
        res = [0]

        n = len(nums)
        for i in range(0, n):
            if nums[i] == 0:
                left_score+=1
            else:
                right_score-=1

            current_score = left_score + right_score

            if current_score > max_score:
                res = []
                max_score = current_score
                res.append(i+1)
            elif current_score == max_score:
                res.append(i+1)

        return res
