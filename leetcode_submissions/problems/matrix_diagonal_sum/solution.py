class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = sum(mat[i][i] + mat[i][len(mat)-i-1] for i in range(len(mat)))
        if len(mat) % 2 == 1:
            center_index = len(mat) // 2
            res -= mat[center_index][center_index]
        return res
