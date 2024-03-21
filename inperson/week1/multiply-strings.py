class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_with(num: int) -> int:
            r = 0
            ans = ""

            for i in range(len(num1)-1, -1, -1):
                digit = (int(num1[i])*num + r)
                ans = str(digit % 10) + ans
                r = digit // 10 if digit > 9 else 0
            return int(str(r) + ans)

        ans = 0

        for i in range(len(num2)-1, -1, -1):
            ans = 10**(len(num2)-i-1) * multiply_with(int(num2[i])) + ans

        return str(ans)