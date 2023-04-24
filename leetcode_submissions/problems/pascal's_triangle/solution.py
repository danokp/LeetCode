class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        result_list = [[1], [1, 1]]
        if numRows == 2:
            result_list
        for i in range(numRows-2):
            previous_row =result_list[-1]
            row = [1]
            for j in range(i+1):
                row.append(previous_row[j] + previous_row[j+1])
            row.append(1)
            result_list.append(row)
        return result_list