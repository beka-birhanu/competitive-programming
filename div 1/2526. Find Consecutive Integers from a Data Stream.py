class DataStream:
    def __init__(self, value: int, k: int):
        self.dq = deque()
        self.k = k
        self.val= value
    def consec(self, num: int) -> bool:
        for i in range(len(self.dq)-self.k+1):
            self.dq.popleft()
        if num != self.val:
            self.dq = deque()
        else:
            self.dq.append(num)
        return len(self.dq) == self.k
