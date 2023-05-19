class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        prev_row = matrix[0]
        for i, row in enumerate(matrix[1:]):
            if prev_row[:-1] != row[1:]:
                return False
            prev_row = row
        return True