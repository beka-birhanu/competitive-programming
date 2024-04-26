# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(swappable_groups, i):
            while swappable_groups_repr[i] != i:
                swappable_groups_repr[i] = swappable_groups_repr[swappable_groups[i]]
                i = swappable_groups_repr[i]
            
            return i

        n = len(s)
        swappable_groups_repr = [i for i in range(n)]

        for a, b in pairs:
            p_a = find(swappable_groups_repr, a)
            p_b = find(swappable_groups_repr, b)

            swappable_groups_repr[p_a] = p_b
        
        swappable_groups = defaultdict(list)
        for i in range(n):
            p = find(swappable_groups_repr, i)
            heappush(swappable_groups[p], s[i])
        
        min_s = []
        for i in range(n):
            p = find(swappable_groups_repr, i)
            min_s.append(heappop(swappable_groups[p]))
        
        return "".join(min_s)


