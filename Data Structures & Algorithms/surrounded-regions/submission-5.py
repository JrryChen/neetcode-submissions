class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(r, c, visited):
            if (r, c) in visited:
                return False
            if not (0 <= r < m) or not (0 <= c < n):
                return True
            if board[r][c] == 'X':
                return False
            visited.add((r, c))    
            return dfs(r + 1, c, visited) or dfs(r - 1, c, visited) or dfs(r, c + 1, visited) or dfs(r, c - 1, visited)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    if not dfs(r, c, set()):
                        board[r][c] = 'X' 

                            
                                   