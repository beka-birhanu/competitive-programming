class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s, d = min(start, destination), max(start, destination)
        return min(sum(distance[s:d]), sum(distance) - sum(distance[s:d]))