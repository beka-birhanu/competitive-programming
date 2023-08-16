class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def binary_search(lst,trgt):
            l,r = 0,len(lst)-1
            while l <= r:
                mid = (l+r)//2
                if lst[mid] > trgt:
                    r = mid-1
                else:
                    l = mid + 1

            return len(lst)-l 

        for idx in range(len(words)):
            smallest = "z"
            val = 0
            for l in words[idx]:
                if l < smallest:
                    val = 1
                    smallest = l
                elif l == smallest:
                    val += 1
            words[idx] = val
        words.sort()


        for idx in range(len(queries)):
            smallest = "z"
            val = 0
            for l in queries[idx]:
                if l < smallest:
                    val = 1
                    smallest = l
                elif l == smallest:
                    val += 1
    
            queries[idx] = binary_search(words,val)
        return queries
