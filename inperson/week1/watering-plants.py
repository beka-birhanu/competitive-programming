class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = len(plants) # at least we need to move thourgh out the list

        # tracking for refills
        current_capacity = capacity

        for i in range(len(plants)):

            if plants[i] > current_capacity:
                steps += 2*i
                current_capacity = capacity

            current_capacity -= plants[i]
            
        return steps
            