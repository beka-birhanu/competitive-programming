class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split(' ')
        output = ''
        for i  in range(1,len(x)+1):
            for j in x:
                if j[-1]== str(i):
                  output+=j[:-1] + ' ' 
        return output[:-1]