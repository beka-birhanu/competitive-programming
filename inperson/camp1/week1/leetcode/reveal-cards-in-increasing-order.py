class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        dq = deque()
        
        for card in deck:
            if len(dq) >= 2:
                dq.appendleft(dq.pop())

            dq.appendleft(card)
        
        return dq