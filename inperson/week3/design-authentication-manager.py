class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = defaultdict(int)
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive



    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0      
        expired = set() 
        for tokenId, timeToExpire in self.tokens.items():
            if timeToExpire > currentTime:
                cnt += 1
            else:
                expired.add(tokenId)
        for tokenId in expired:
            del self.tokens[tokenId]
        return cnt

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)