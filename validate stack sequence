class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed_stack = []
        for p in pushed:
            pushed_stack.append(p)
            while pushed_stack and popped and pushed_stack[-1] == popped[0]:
                popped.pop(0)
                pushed_stack.pop()
        return pushed_stack == []
