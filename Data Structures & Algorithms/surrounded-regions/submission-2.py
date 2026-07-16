class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        visited = set()

        def dfs(r, c):
            if not (0 <= r < ROW) or not (0 <= c < COL):
                return
            if (r,c) in visited or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROW):
            if board[r][0] == 'O' and (r, 0) not in visited:
                dfs(r, 0)
            if board[r][COL - 1] == 'O' and (r, COL - 1) not in visited:
                dfs(r, COL - 1)
        print(board)
        for c in range(COL):
            if board[0][c] == 'O' and (0, c) not in visited:
                dfs(0, c)
            if board[ROW - 1][c] == 'O' and (ROW - 1, c) not in visited:
                dfs(ROW - 1, c)
        print(board)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'


            
