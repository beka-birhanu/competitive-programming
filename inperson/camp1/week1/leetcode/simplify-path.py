class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for folder in path.split('/'):
            if folder not in ['','.','..']:
                s.append(folder) 
            elif folder=='..' and s:
                    s.pop()   
        return  '/'+('/').join(s)