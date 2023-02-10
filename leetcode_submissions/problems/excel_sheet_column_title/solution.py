class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = []
        while columnNumber > 0:
            result.append((columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
        return ''.join(map(
            lambda x: letters[x],
            result[::-1]
        ))