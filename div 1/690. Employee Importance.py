"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# Runtime 20% , Memory 92%
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def findAndCollect(i):
            stack = [i]
            total = 0
            while stack:
                employee = employees[stack.pop()]
                total += employee.importance
                for sub in employee.subordinates:
                    stack.append(find(sub))
            return total



        def find(id):
            for i in range(len(employees)):
                if employees[i].id == id:
                    return i
        return findAndCollect(find(id))


# Runtime 95% , Memory 50%
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def findAndCollect(boss):
            stack = [boss]
            total = 0
            while stack:
                emp = stack.pop()
                total += emp.importance
                for sub in emp.subordinates:
                    stack.append(idMapEmp[sub])
            return total

        idMapEmp = {}
        for emp in employees:
            idMapEmp[emp.id] = emp
            if emp.id == id:
                boss = emp
        return findAndCollect(find(id))

# Rumtime 80% , Memory 79%
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def findAndCollect(boss):
            stack = [boss]
            total = 0
            while stack:
                emp = stack.pop()
                total += emp.importance
                del[idMapEmp[emp.id]]
                for sub in emp.subordinates:
                    stack.append(idMapEmp[sub])
            return total



        idMapEmp = {}
        for emp in employees:
            idMapEmp[emp.id] = emp

        return findAndCollect(idMapEmp[id])
