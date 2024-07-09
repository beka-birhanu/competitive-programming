# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

public class Solution {
    public int LastStoneWeight(int[] stones) {
        PriorityQueue<int, int> pStones = new();
        for (int i = 0; i < stones.Length; i++) {
            pStones.Enqueue(stones[i], -stones[i]);
        }

        while (pStones.Count > 1) {
            int stoneOne = pStones.Dequeue();
            int stoneTwo = pStones.Dequeue();
            int diff = stoneOne-stoneTwo;
            
            if (diff > 0) pStones.Enqueue(diff, -diff);
        }

        return pStones.Count > 0? pStones.Dequeue() : 0;
    }
}