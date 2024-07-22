# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

public class Solution {
    public int WateringPlants(int[] plants, int capacity) {
        int steps = 0;
        int currentCapacity = capacity;

        for(int i = 0; i < plants.Length; i++) {
            steps++;
            if(currentCapacity < plants[i]) {
                steps += 2*i;
                currentCapacity = capacity;
            }
            currentCapacity -= plants[i];
        }

        return steps;
    }
}