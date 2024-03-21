class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
       
        def comb(n, m):
            @cache 
            def factorial(n):
                if n == 1:
                    return 1

                return n * factorial(n-1)
            

            if n == m or m == 0:
                return 1
            else:
                return factorial(n) // (factorial(m)*factorial(n-m))
        
        return [comb(rowIndex,i) for i in range(0, rowIndex+1) ]