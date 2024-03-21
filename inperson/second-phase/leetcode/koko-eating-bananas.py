class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k, piles, h):
            curr_pile = 0
            curr_h = 0

            while curr_pile < len(piles):
                curr_h += math.ceil(piles[curr_pile]/k)
                if curr_h > h :
                    break

                curr_pile += 1


            return curr_pile == len(piles)

        _min = math.ceil(sum(piles)/h)
        _max = max(piles)
        
        if h == len(piles):
            return _max

        while _min < _max:
            k = (_min + _max)//2
            if possible(k, piles, h):
                _max = k
            
            else:
                _min = k + 1

        return _max