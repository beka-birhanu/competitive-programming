class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = set(["+","-","*","/"])
        for n in tokens:
            if n not in ops:
                nums.append(n)
            else:
                oprand2 = int(nums.pop())
                oprand1 = int(nums.pop())
                if n == '+':
                    ans = oprand1 + oprand2
                elif n == '-':
                    ans = oprand1 - oprand2
                elif n== '*':
                    ans = oprand1 * oprand2
                else:
                     ans = int(oprand1 / oprand2)
                nums.append(ans)
        return int(nums[0])