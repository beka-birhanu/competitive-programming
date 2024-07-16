# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        representation = defaultdict(list)
        for i in range(len(equations)):
            a,b = equations[i]
            representation[a].append((b,values[i]))
            representation[b].append((a,1/values[i]))

        def search(start, target):
            visited = set([start])
            stack = [(start,1)]
            while stack:
                var,path = stack.pop()
                for var2,ratio in representation[var]:
                    if var2 == target:
                        return path*ratio
                    if var2 not in visited:
                        stack.append((var2,path*ratio))
                        visited.add(var2)
            return -1.0

        ans = [0]*len(queries)
        for i in range(len(queries)):
            a,b = queries[i]
            ans[i] = search(a,b)

        return ans
            
