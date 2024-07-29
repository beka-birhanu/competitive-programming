# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()

        curr_max_profit = 0
        total_profit = 0
        j = 0
        for w in range(len(worker)):
            ability = worker[w]
            while j < len(jobs) and jobs[j][0] <= ability:
                curr_max_profit = max(curr_max_profit, jobs[j][1])
                j += 1

            total_profit += curr_max_profit
        
        return total_profit
        