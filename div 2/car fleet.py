class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        given = [(i,j) for i,j in zip(position,speed)]
        given.sort(reverse = True)
        stack = []
        for s,v in given:
            totall_time = (target - s) / v
            if not stack or totall_time > stack[-1]:
                stack.append(totall_time)
        return len(stack)
