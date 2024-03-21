class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0]*n
        self.curently_at = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        stoped_before = self.curently_at
        while self.curently_at < len(self.stream) and self.stream[self.curently_at] != 0:
            self.curently_at += 1
        
        return self.stream[stoped_before:self.curently_at]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)