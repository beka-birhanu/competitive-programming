# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	m := len(meetings)
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][2] < meetings[j][2]
	})

	graph := constructor(n)
	graph.unite(firstPerson, 0)

	idx := 0
	jdx := 0
	time := meetings[0][2]
	for idx < m {
		for idx < m && meetings[idx][2] == time {
			graph.unite(meetings[idx][0], meetings[idx][1])
			idx++
		}

		for jdx < idx {
			if !graph.connected(meetings[jdx][0], 0) {
				graph.reset(meetings[jdx][0])
				graph.reset(meetings[jdx][1])
			}
			jdx++
		}

		if idx < m {
			time = meetings[idx][2]
		}
	}
	answer := []int{}
	for i := 0; i < n; i++ {
		if graph.connected(i, 0) {
			answer = append(answer, i)
		}
	}

	return answer
}

type UnionFind struct {
	parent []int
}

func constructor(n int) UnionFind {
	parent := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
	}

	return UnionFind{parent}
}

func (this *UnionFind) find(x int) int {
	if this.parent[x] != x {
		this.parent[x] = this.find(this.parent[x])
	}
	return this.parent[x]
}

func (this *UnionFind) unite(x, y int) {
	px := this.find(x)
	py := this.find(y)
	if px != py {
		this.parent[py] = px
	}
}

func (this *UnionFind) connected(x, y int) bool {
	return this.find(x) == this.find(y)
}

func (this *UnionFind) reset(x int) {
	this.parent[x] = x
}