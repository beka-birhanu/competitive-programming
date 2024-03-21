class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        intersections = []

        while p1 < len(firstList) and p2 < len(secondList):
            
            intersection = [max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])]

            # check if the intersection is valid
            if intersection[0] <= intersection[1]:
                intersections.append(intersection)

            # move the pointers if we passed the intersection
            if firstList[p1][1] <= intersection[1]:
                p1+=1

            if secondList[p2][1] <= intersection[1]:
                p2+=1

        return intersections