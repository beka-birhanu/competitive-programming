# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

func corpFlightBookings(bookings [][]int, n int) []int {
    totalBookings := make([]int, n+1)

    for _, booking := range bookings {
        first, last, seats := booking[0], booking[1], booking[2]
        totalBookings[first-1] += seats
        totalBookings[last] -= seats
    }

    for i := 1; i < n; i++ {
        totalBookings[i] += totalBookings[i-1]
    }
    return totalBookings[:n]
}