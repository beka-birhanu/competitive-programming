class Solution:
    def getRow_recursive(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = self.getRow_recursive(rowIndex - 1)
        row = [1]
        for i in range(1, rowIndex):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        return row
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row
