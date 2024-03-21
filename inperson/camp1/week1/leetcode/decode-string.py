class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        pre = [] #the part where there is no need for decding 
        for i in range(len(s)):
            if s[i].isdigit() or s[i] == "[":
                break
            
            pre.append(s[i])

        i = len(pre)
        while i < len(s):
            if not s[i].isdigit():
                break
            i += 1
        
        multiplier = int(s[len(pre):i] if i > len(pre) else 1)
        curr = []  #the part that is going to be decoded now

        #go through the string until the brackets balance
        opens = 1
        i += 1
        while i < len(s):
            if s[i] == "]":
                opens -= 1
            if s[i] == "[":
                opens += 1

            if not opens:
                break
            curr.append(s[i])
            i += 1
        
        return "".join(pre) + (self.decodeString("".join(curr)) * multiplier) + self.decodeString(s[i+1:])
