class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        meta_shift = [0]*(len(s)+1)
        for start,end, direction in shifts:
            if direction == 0:
                direction = -1
            meta_shift[start] += direction
            meta_shift[end+1] -= direction

        for i in range(1,len(s)):
            meta_shift[i] += meta_shift[i-1]
        
        s = list(s)
        
        for i in range(len(s)):
            asci = ord(s[i])+meta_shift[i]
            if asci > 122:
                asci = 97 + (asci - 123)%26
            elif asci < 97:
                asci = 122 - (96 - asci)%26

            s[i] = chr(asci)

        return "".join(s)