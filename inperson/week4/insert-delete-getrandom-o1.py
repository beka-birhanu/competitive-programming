class RandomizedSet:

    def __init__(self):
        # stores values mapped to their index, 
        # this is for making insetion and removing in constant time
        self.map = {}

        # stores values, this for geting a random value 
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.values)
            self.values.append(val)        
            return True
        return False


    def remove(self, val: int) -> bool:
        if val  in self.map:
            # store the index of value
            idx = self.map[val]

            # swap the val to the end and pop
            self.values[idx], self.values[len(self.values)-1] = self.values[len(self.values)-1], self.values[idx]
            self.values.pop()

            # delte the val form map and apdate the index of the swaped element 
            del self.map[val]

            if idx < len(self.values):
                self.map[self.values[idx]] = idx
            return True
        return False

    def getRandom(self) -> int:
        return self.values[random.randint(0,len(self.values)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()