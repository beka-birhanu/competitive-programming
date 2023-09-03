class Solution:
    def hIndex(self, citations: List[int]) -> int:
        greater = []
        citations.sort(reverse=True)
        for i in range(len(citations),-1,-1):
            while citations and citations[0] >= i:
                greater.append(citations.pop(0))
            if len(greater) >= i:
                return i
