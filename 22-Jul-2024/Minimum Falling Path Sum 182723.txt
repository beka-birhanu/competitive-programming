# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

func minFallingPathSum(matrix [][]int) int {
	n := len(matrix)
	dp := make([]int, n)
	copy(dp, matrix[0])

	for i := 1; i < n; i++ {
		temp := make([]int, n)
		for j := 0; j < n; j++ {
			minVal := dp[j]
			if j > 0 {
				minVal = min([]int{minVal, dp[j-1]})
			}
			if j < n-1 {
				minVal = min([]int{minVal, dp[j+1]})
			}
			temp[j] = minVal + matrix[i][j]
		}
		copy(dp, temp)
	}
    
	return min(dp)
}

func min(slice []int) int {
	if len(slice) == 0 {
		panic("cannot find the minimum of an empty slice")
	}

	minVal := slice[0]
	for _, value := range slice[1:] {
		if value < minVal {
			minVal = value
		}
	}

	return minVal
}