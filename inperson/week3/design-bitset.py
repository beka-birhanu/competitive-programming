class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.ones= set()
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if idx in self.ones:
                self.ones.remove(idx)
        else:
            self.ones.add(idx)

    def unfix(self, idx: int) -> None:
        
        if self.flipped:
            self.ones.add(idx)
        else:
            if idx in self.ones:
                self.ones.remove(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        return self.count() == self.size

    def one(self) -> bool:
        return self.count() > 0

    def count(self) -> int:
        if self.flipped:
            return self.size - len(self.ones)
        return len(self.ones)

    def toString(self) -> str:
        bitset = ["0"]*self.size
        if self.flipped:
            for i in range(self.size):
                if i not in self.ones:
                    bitset[i] = "1"
        else:
            for i in range(self.size):
                if i in self.ones:
                    bitset[i] = "1"
        return "".join(bitset)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()