from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-val for val in count.values()]
        heapq.heapify(maxHeap)
        dq = deque()
        time = 0
        while dq or maxHeap:
            time+=1
            if maxHeap:
                task_left = heapq.heappop(maxHeap) + 1
                if task_left:
                    dq.append([task_left, time+n])
            if dq and dq[0][1] ==  time:
                heapq.heappush(maxHeap,dq.popleft()[0])
        return time
