class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        min_hp, max_hp = [], []

        for i in range(len(weights)-1):           
            pair = weights[i] + weights[i+1]

            heapq.heappush(min_hp, -pair)
            heapq.heappush(max_hp, pair)

            if len(max_hp) > (k - 1):
                heapq.heappop(min_hp)
                heapq.heappop(max_hp)
        
        return sum(max_hp) - (-sum(min_hp))