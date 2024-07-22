# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

func sortPeople(names []string, heights []int) []string {
	n := len(names)
	people := make([]struct {
		name   string
		height int
	}, n)

	for i := 0; i < n; i++ {
		people[i].name = names[i]
		people[i].height = heights[i]
	}

	sort.Slice(people, func(i, j int) bool {
		return people[i].height > people[j].height
	})

	for i := 0; i < n; i++ {
		names[i] = people[i].name
	}

	return names
}