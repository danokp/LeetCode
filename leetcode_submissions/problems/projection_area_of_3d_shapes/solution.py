class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_proj_area = 0
        yz_proj_area = 0

        max_col = grid[0]
        for row in grid:
            max_in_row = row[0]
            for index, num in enumerate(row):
                if num > max_col[index]:
                    max_col[index] = num
                if num > max_in_row:
                    max_in_row = num
                if num > 0:
                    xy_proj_area += 1
            yz_proj_area += max_in_row

        zx_proj_area = sum(max_col)

        return xy_proj_area + yz_proj_area + zx_proj_area