class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def sum_hourglass(i,j):
            _sum = 0
            for di,dj in [(0,0),(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]:
                _sum += grid[i+di][j+dj]
            return _sum

        _max = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                _max = max(_max, sum_hourglass(i,j))
        return _max