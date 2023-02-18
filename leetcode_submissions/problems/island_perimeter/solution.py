class Solution:
    def islandPerimeter(self, grid) -> int:
        def calc_addition(cell_value):
            if cell_value == 0:
                return 1
            return 0
        perimeter = 0
        for i_row, row in enumerate(grid):
            for j_col, cell in enumerate(row):
                if cell == 1:
                    add_to_perimeter = [
                        calc_addition(grid[i_row - 1][j_col] if i_row - 1 >= 0 else 0), # top
                        calc_addition(grid[i_row + 1][j_col] if i_row + 1 < len(grid) else 0), # bot 
                        calc_addition(grid[i_row][j_col - 1] if j_col - 1 >= 0 else 0), # left
                        calc_addition(grid[i_row][j_col + 1] if j_col + 1 < len(row) else 0), # right
                    ]
                    perimeter += sum(add_to_perimeter)
        return perimeter