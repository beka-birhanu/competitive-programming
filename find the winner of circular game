class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        frds = [i for i in range(1,n+1)]
        i = 0
        while len(frds) > 1:
            if (i+k-1) >= len(frds):
                looser_place = (i+k-1)%len(frds)
            else:
                looser_place = i+k-1
            looser = frds[looser_place]
            frds.remove(looser)
            i = looser_place
        return frds[0]
