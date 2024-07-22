# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
	calcPositions := func(graph [][]int, dependency []int) map[int]int {
		queue := list.New()
		for i := 1; i <= k; i++ {
			if dependency[i] == 0 {
				queue.PushBack(i)
			}
		}

		positions := make(map[int]int)
		for queue.Len() > 0 {
			node := queue.Front()
			queue.Remove(node)
			n := node.Value.(int)
			positions[n] = len(positions)

			for _, child := range graph[n] {
				dependency[child] -= 1
				if dependency[child] == 0 {
					queue.PushBack(child)
				}
			}
		}
		return positions
	}

	buildMatrix := func(rowPositions, colPositions map[int]int, k int) [][]int {
		matrix := make([][]int, k)
		for i := range matrix {
			matrix[i] = make([]int, k)
		}
		for i := 1; i <= k; i++ {
			row := rowPositions[i]
			col := colPositions[i]
			matrix[row][col] = i
		}
		return matrix
	}

	rowGraph := make([][]int, k+1)
	colGraph := make([][]int, k+1)
	rowDependency := make([]int, k+1)
	colDependency := make([]int, k+1)

	for _, condition := range rowConditions {
		parent, child := condition[0], condition[1]
		rowGraph[parent] = append(rowGraph[parent], child)
		rowDependency[child] += 1
	}

	for _, condition := range colConditions {
		parent, child := condition[0], condition[1]
		colGraph[parent] = append(colGraph[parent], child)
		colDependency[child] += 1
	}

	rowPositions := calcPositions(rowGraph, rowDependency)
	if len(rowPositions) != k {
		return [][]int{}
	}

	colPositions := calcPositions(colGraph, colDependency)
	if len(colPositions) != k {
		return [][]int{}
	}

	return buildMatrix(rowPositions, colPositions, k)
}
