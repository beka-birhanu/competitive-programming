# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        affordable = []
        non_affordable = []
        for p, c in zip(profits, capital):
            if c <= w:
                heapq.heappush(affordable, -p)
            
            else:
                non_affordable.append((c, p))
        
        non_affordable.sort(reverse=True)
        i = 0
        while i < k:
            while non_affordable and non_affordable[-1][0] <= w:
                heapq.heappush(affordable, -non_affordable.pop()[1])

            if not affordable:
                break

            w -= heapq.heappop(affordable)
            i += 1
        
        return w