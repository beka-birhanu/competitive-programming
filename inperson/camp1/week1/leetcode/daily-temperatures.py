class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for D, T in enumerate(temperatures):

            while stack and T > stack[-1][1]:
                day, temp = stack.pop()
                wait_D = D - day
                ans[day] = wait_D

            stack.append((D, T))
        return ans