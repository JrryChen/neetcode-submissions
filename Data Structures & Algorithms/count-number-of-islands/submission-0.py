class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        def dfs(r, c):
            if grid[r][c] == '0':
                return
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                    continue
                if (x, y) in seen:
                    continue
                if grid[x][y] == '1':
                    seen.add((x, y))
                    dfs(x, y)       

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in seen:
                    res += 1
                    dfs(r, c)
        return res