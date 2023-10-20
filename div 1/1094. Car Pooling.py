class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips,key=lambda x: x[2])[2]
        arr = [0]*(n+1)
        for P,start,end in trips:
            arr[start] += P
            arr[end]-= P

        on_board = 0
        for num in arr:
            on_board += num
            if on_board > capacity:
                return False

        return True
