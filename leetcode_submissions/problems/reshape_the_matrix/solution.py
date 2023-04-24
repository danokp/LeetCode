class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) != r * c:
            return mat
        one_line_mat = [item for row in mat for item in row]
        res = []
        for i in range(0, r*c, c):
            res.append(one_line_mat[i:i+c])
        print(res)
        return res