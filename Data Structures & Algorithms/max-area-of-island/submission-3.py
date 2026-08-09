class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        seen = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            if not grid[r][c]:
                return 0
            count = 1
            for dx, dy in directions:
                x, y = r + dx, c + dy
                if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
                    continue
                if (x, y) in seen:
                    continue
                if grid[x][y]:
                    seen.add((x, y))
                    count += dfs(x, y)
            return count        


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] and (r, c) not in seen:
                    seen.add((r, c))
                    max_area = max(max_area, dfs(r, c))    

        return max_area