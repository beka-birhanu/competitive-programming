# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        if len(stones) == 2:
            return True
            
        dp = [set() for _ in range(len(stones))]
        
        for i in range(len(stones)-2, -1, -1):
            for j in range(i+1, len(stones)):
                diff = stones[j]-stones[i]
                
                if diff in dp[j] or j == len(stones)-1:
                    dp[i].add(diff)
                    dp[i].add(diff+1)
                    dp[i].add(diff-1)
        print(dp)
        return 1 in dp[1]