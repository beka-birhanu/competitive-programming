class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(math.sqrt(c)) + 1
        i = 0
        while i <= j:
            t = i*i + j*j
            if t == c:
                return True
            if t > c:
                j -= 1
            else:
                i += 1
        return False
