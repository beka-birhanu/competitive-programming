class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            d = {')':'(','}':'{',']':'['}
            opens = []
            for p in s:
                if p in d:
                    if opens and opens[-1] == d[p]:
                        opens.pop()
                    else:
                        return False
                else:
                    opens.append(p)
            return True if not opens else False