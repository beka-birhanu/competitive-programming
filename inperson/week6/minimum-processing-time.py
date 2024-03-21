class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse= True)
        time = 0
        for i in range(0,len(tasks),4):
            time = max(tasks[i] + processorTime[i//4],time)
        return time