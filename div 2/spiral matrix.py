class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r_end = len(matrix) - 1
        c_end = len(matrix[0]) - 1
        r_start, c_start = 0, 0
        ans = []
        while r_start <= r_end and c_start <= c_end:
            for i in range(c_start,c_end+1):
                ans.append(matrix[r_start][i])
            r_start += 1
            for i in range(r_start,r_end+1):
                ans.append(matrix[i][c_end])
            c_end -= 1
            if r_end >= r_start:
                for i in range(c_end, c_start-1, -1):
                    ans.append(matrix[r_end][i])
            r_end -= 1
            if c_end >= c_start:
                for i in range(r_end, r_start-1, -1):
                    ans.append(matrix[i][c_start])
            c_start += 1

        return ans
