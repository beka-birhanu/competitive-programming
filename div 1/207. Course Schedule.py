# Runtime 105ms and Memory 17.7 mb
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            stack = [course]
            q = []
            while stack:
                course = stack.pop()
                if course == -1:
                    color[q.pop()] = -1
                    continue
                else:
                    q.append(course)
                    color[course] = 1  
                    stack.append(-1)         
                for p in adj[course]:
                    if color[p] == 1:
                        return True
                    if color[p] == 0:
                        stack.append(p)
                

            return False

        color = [0] * numCourses
        adj = defaultdict(list)
        for p in prerequisites:
            a,b = p
            adj[a].append(b)

        for i in range(numCourses):
            if not color[i] and dfs(i): return False
        return True
