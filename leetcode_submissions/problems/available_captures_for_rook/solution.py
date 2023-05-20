class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def find_rook_coord(board):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == 'R':
                        return i, j

        coord_x, coord_y = find_rook_coord(board)
        capture_count =0

        for i in range(coord_x, -1, -1):
            if board[i][coord_y] == 'B':
                break
            if board[i][coord_y] == 'p':
                capture_count += 1
                break
        for i in range(coord_x, 8):
            if board[i][coord_y] == 'B':
                break
            if board[i][coord_y] == 'p':
                capture_count += 1
                break

        for i in range(coord_y, -1, -1):
            if board[coord_x][i] == 'B':
                break
            if board[coord_x][i] == 'p':
                capture_count += 1
                break
        for i in range(coord_y, 8):
            if board[coord_x][i] == 'B':
                break
            if board[coord_x][i] == 'p':
                capture_count += 1
                break
        return capture_count