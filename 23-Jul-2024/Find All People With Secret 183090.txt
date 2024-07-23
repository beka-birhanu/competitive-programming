# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	meetingGraph := make([][][2]int, n)
	for _, meeting := range meetings {
		person1, person2, time := meeting[0], meeting[1], meeting[2]
		meetingGraph[person1] = append(meetingGraph[person1], [2]int{person2, time})
		meetingGraph[person2] = append(meetingGraph[person2], [2]int{person1, time})
	}

	hearingTime := make([]int, n)
	for i := range hearingTime {
		hearingTime[i] = -1
	}
	hearingTime[0] = 0
	hearingTime[firstPerson] = 0

	stack := []int{firstPerson, 0}

	for len(stack) > 0 {
		person1 := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		for _, neighbor := range meetingGraph[person1] {
			person2, meetingTime := neighbor[0], neighbor[1]
			if hearingTime[person2] != -1 && hearingTime[person2] <= meetingTime {
				continue
			}

			if meetingTime >= hearingTime[person1] {
				hearingTime[person2] = meetingTime
				stack = append(stack, person2)
			}
		}
	}

	heardSecret := []int{}
	for person, time := range hearingTime {
		if time >= 0 {
			heardSecret = append(heardSecret, person)
		}
	}

	return heardSecret
}
