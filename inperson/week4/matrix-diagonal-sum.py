class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0


        for i in range(len(mat)):
            
            _sum += mat[i][i] + mat[i][len(mat)-i-1]
        return _sum - mat[len(mat)//2][len(mat)//2] if len(mat)%2 else _sum
