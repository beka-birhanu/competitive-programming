# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

func numberOfPairs(nums1 []int, nums2 []int, diff int) int64 {
    differences := make([]int, len(nums1))
    
    for i := range nums1 {
        differences[i] = nums1[i] - nums2[i]
    }

    _, count := mergeSortAndCount(differences, diff)
    return count
}

func mergeSortAndCount(nums []int, diff int) ([]int, int64) {
    if len(nums) <= 1 {
        return nums, 0
    }

    mid := len(nums) / 2
    leftList, leftCount := mergeSortAndCount(nums[:mid], diff)
    rightList, rightCount := mergeSortAndCount(nums[mid:], diff)

    mergedList, mergingCount := mergeAndCount(leftList, rightList, diff)

    return mergedList, leftCount + rightCount + mergingCount
}

func mergeAndCount(leftList, rightList []int, diff int) ([]int, int64) {
    mergedList := make([]int, 0, len(leftList)+len(rightList))
    var count int64 = 0
    l, r := 0, 0

    for l < len(leftList) && r < len(rightList) {
        if leftList[l] < rightList[r] {
            _min := leftList[l] - diff
            pos := lowerBound(rightList, _min)
            count += int64(len(rightList) - pos)
            mergedList = append(mergedList, leftList[l])
            l++
        } else {
            mergedList = append(mergedList, rightList[r])
            r++
        }
    }

    for l < len(leftList) {
        _min := leftList[l] - diff
        pos := lowerBound(rightList, _min)
        count += int64(len(rightList) - pos)
        mergedList = append(mergedList, leftList[l])
        l++
    }

    for r < len(rightList) {
        mergedList = append(mergedList, rightList[r])
        r++
    }

    return mergedList, count
}

func lowerBound(a []int, x int) int {
    return sort.Search(len(a), func(i int) bool { return a[i] >= x })
}
