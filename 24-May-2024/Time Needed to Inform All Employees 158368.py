# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinate_graph = [[] for _ in range(n)]

        for subordinate_id, manager_id in enumerate(manager):
            if manager_id == -1:
                continue
            
            subordinate_graph[manager_id].append(subordinate_id)
        
        queue = deque([(0, headID)])
        max_time = 0

        while queue:
            hearing_time, id = queue.pop()

            if not subordinate_graph[id]:
                max_time = max(max_time, hearing_time)
            
            telling_time = hearing_time + informTime[id]
            for subordinate_id in subordinate_graph[id]:
                queue.append((telling_time, subordinate_id))
        
        return max_time
