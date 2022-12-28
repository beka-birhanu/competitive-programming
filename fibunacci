class Solution:
    def fib(self, n: int) -> int:
        num = [0,1]
        if n <= 1:
            return num[n]
        for i in range(1,n):
            num.append(num[-1]+num[-2])
        return num[-1] 
