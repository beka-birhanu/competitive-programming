# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        Array.Sort(players);
        Array.Sort(trainers);

        var i = players.Length -1;
        var j = trainers.Length -1;
        var count = 0;
        while(i > -1 && j > -1){
            if (players[i] > trainers[j]){
                i--;
                continue;
            }
            count++;
            i--;
            j--;

        }
        return count;
    }
}