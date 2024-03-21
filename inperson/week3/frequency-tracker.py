class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_of_freq = defaultdict(int)

    def add(self, number: int) -> None:
        if  self.freq_of_freq[self.freq[number]]:
            self.freq_of_freq[self.freq[number]] -= 1
        self.freq[number] += 1
        self.freq_of_freq[self.freq[number]] += 1
    def deleteOne(self, number: int) -> None:

        if self.freq[number]:
            self.freq_of_freq[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.freq_of_freq[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return  self.freq_of_freq[frequency] > 0
     


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)