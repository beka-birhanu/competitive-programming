class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        booked = [0]*(n+1)
        
        for first, last, seats in bookings:
            booked[first-1] += seats
            booked[last] -= seats
        
        booked.pop()
        return accumulate(booked)