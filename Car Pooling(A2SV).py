class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[2])
        trips.sort(key = lambda x:x[1])

        on_board = {}
        prv= []
        totall = 0
        for p,start,end in trips:

            while len(prv) and prv[0] <= start:
                dropped = heapq.heappop(prv)
                totall -= on_board[dropped]
                del on_board[dropped]

            totall += p
            if totall > capacity:
                return False
            
            if end in on_board:
                on_board[end] += p
            else:
                on_board[end] = p
                heapq.heappush(prv,end)

        return True
