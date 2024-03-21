class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = set() # store players with any win
        losers_one_times = set() # stores players exactly with any lose
        losers_more_times = set() # stores players with more than one loses

        for winner, loser in matches:
            winners.add(winner)
            if loser in losers_one_times:
                losers_more_times.add(loser)
            losers_one_times.add(loser)
            
        """
        no lose = any win - any lose
        one lose = any lose - many lose
        """
        return [sorted(list(winners- losers_one_times)),sorted(list(losers_one_times-losers_more_times))]