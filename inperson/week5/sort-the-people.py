class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = size = len(names)-1
        not_sorted = True
        while size > 0 and not_sorted:
            n = len(names)-1
            not_sorted = False
            while n > 0:
                if heights[n] > heights[n-1]:
                    heights[n],heights[n-1] = heights[n-1],heights[n]
                    names[n],names[n-1] = names[n-1],names[n]
                    not_sorted = True
                n -= 1
            size -= 1
        return names