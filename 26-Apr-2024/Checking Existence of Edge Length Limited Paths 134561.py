# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(parents, i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]
                i = parents[i]
            
            return i
        
        for i, query in enumerate(queries):
            query.append(i)

        parents = [i for i in range(n)]
        queries.sort(key = lambda x : x[-2])
        edgeList.sort(key = lambda x : x[-1])

        j = 0

        ans = [False] * len(queries)
        for p, q, limit, i in queries:
            while j < len(edgeList):
                u, v, dis = edgeList[j]
                
                if limit <= dis:
                    break

                p_u = find(parents, u)
                p_v = find(parents, v)
                parents[p_u] = p_v
                
                j += 1

            ans[i] = find(parents, p) == find(parents, q)

        return ans

