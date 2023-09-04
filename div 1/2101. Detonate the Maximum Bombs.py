# Runtime 723ms and Memory 16.6mb
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(i):
            stack = [i]
            count = 0
            visited = set(stack)
            while stack:

                i = stack.pop()
                count += 1
                for j in adj[i]:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
            return count


        adj = defaultdict(list)
        for i in range(len(bombs)):
            x,y,r = bombs[i]
            for j in range(len(bombs)):
                x2,y2,r2 = bombs[j]
                if(x-x2)**2 + (y-y2)**2 <= r**2 and i != j:
                    adj[i].append(j)

        

        max_ = 0
        v = set()
        for i in range(len(bombs)):
            if i not in v:
                max_ = max(max_, dfs(i))
        return max_
        
