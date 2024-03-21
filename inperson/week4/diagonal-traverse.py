class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m , n = len(mat), len(mat[0])
        def redirect(i:int, j:int, is_upward:bool)->(int,int,bool):
            if is_upward:
                if j < n:
                    return i+1,j,False
                else:
                    return i+2, j-1,False
            else:
                if i < m:
                    return i,j+1, True
                else:
                    return i-1,j+2,True
        
        ans = []
        st = [(0,0,True)]
        while st:
            i,j,is_upward = st.pop()
            if 0 <= i<m and 0 <= j < n:
                ans.append(mat[i][j])
                if is_upward:
                    st.append((i-1,j+1,True))

                else:
                    st.append((i+1,j-1,False))

            else:
                i,j,is_upward = redirect(i,j,is_upward)
                if 0 <= i<m and 0 <= j < n:
                    st.append(( i,j,is_upward))
        return ans 