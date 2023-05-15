class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        while len(row) - 1 < rowIndex:
            row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
        return row