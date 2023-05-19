class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def invert_num(num):
            return 1 if num == 0 else 0

        return [
            [invert_num(num) for num in row[::-1]]
            for row in image
        ]