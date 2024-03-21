class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        idx = [0]*(len(s)+1)
        for i,j,d in shifts:
            if d:
                idx[i] += 1
                idx[j + 1] -= 1

            else:
                idx[i] -= 1
                idx[j + 1] += 1

        s = list(s)
        s[0] = chr((ord(s[0])-97 + idx[0])%26 + 97)
        
        for i in range(1,len(s)):
            idx[i] += idx[i-1]
            s[i] = chr((ord(s[i])-97 + idx[i])%26 + 97)

        return "".join(s)

        