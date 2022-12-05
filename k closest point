def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    min_heap =[]
    def distance(point):
        x = point[0]
        y = point[1]
        d = ((x) ** 2 + (y) ** 2) 
        return [d,x,y]

    def minheap_sorter(points):
        for point in points:
            min_heap.append(distance(point))
        heapq.heapify(min_heap)

    minheap_sorter(points)
    for length in range(k):
        d,x,y = heapq.heappop(min_heap)
        result.append([x,y])

    return result
