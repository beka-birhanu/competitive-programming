class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dict_ = [(1,"0")]
        def invert(s):
            return ''.join('1' if x == '0' else '0' for x in s)
        def generator(n):
            if n == dict_[0][0]:
                return dict_[0][1]
            else:
                dict_[0] = (n,generator(n-1) + "1" + invert(dict_[0][1][::-1]))
                return dict_[0][1]
        return generator(n)[k-1]

    def findKthBit_2(self, n: int, k: int) -> str:
        # it is not necessary to do all the work for the whole bit
        # it  is enough to concider only about one bit at a time 
        
        n = 2 ** n - 1
        flip = 0
        while k > 1:
            if k == n //2 + 1:
                # use XOR to flip the bit
                return str(1 ^ flip)
            
            if k > n //2:
                k = n + 1 - k
                flip = 1- flip
            
            n//= 2
        return str(flip)
