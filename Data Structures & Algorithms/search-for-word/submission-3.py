class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        def dfs(curr, r, c, seen):
            if curr == word:
                return True
            if len(curr) >= len(word):
                return False
            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy
                if not 0 <= new_r < len(board) or not 0 <= new_c < len(board[0]):
                    continue
                if (new_r, new_c) in seen:
                    continue
                seen.add((new_r, new_c))
                ch = board[new_r][new_c]
                if word.startswith(curr + ch):
                    if dfs(curr + ch, new_r, new_c, seen):
                        return True
                seen.remove((new_r, new_c))
            return False
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word:
                    return True
                if word.startswith(board[r][c]):
                    seen = {(r, c)}
                    if dfs(board[r][c], r, c, seen):
                        return True
        return False