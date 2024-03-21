class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()


    def push(self, x: int) -> None:
        self.queue1.append(x)
        
    def pop(self) -> int:
        queue2 = collections.deque()
        x = self.queue1[0]

        for _ in range(len(self.queue1)):
            x = self.queue1.popleft()
            queue2.append(x)

        for _ in range(len(queue2)-1):
            self.queue1.append(queue2.popleft())

        return x

    def top(self) -> int:
        queue2 = collections.deque()
        x = self.queue1[0]

        for _ in range(len(self.queue1)):
            x = self.queue1.popleft()
            queue2.append(x)

        for _ in range(len(queue2)):
            self.queue1.append(queue2.popleft())

        return x

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()