class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ans = 0

        while players and trainers:
            if players[-1] > trainers[-1]:
                players.pop()
            else:
                players.pop()
                trainers.pop()
                ans += 1
        
        return ans

    def matchPlayersAndTrainers_2(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ans = 0
        i = j = 0
        while i < len(players) and j < len(trainers):
            while j < len(trainers) and players[i] > trainers[j]:
                j += 1
            
            if j < len(trainers) and players[i] <= trainers[j]:
                ans += 1
            i += 1
            j += 1
        return ans
