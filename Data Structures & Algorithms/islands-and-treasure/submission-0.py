class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        def dfs(i, r, c):
            if grid[r][c] < 0: # water cell, can't dfs it
                return
            # land cell or treasure chest
            if grid[r][c] > 0: # land cell -> replace with i
                if grid[r][c] <= i:
                    return
                grid[r][c] = i    
            # explore     
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy
                if not (0 <= new_r < m) or not (0 <= new_c < n):
                    # invalid coordinate
                    continue   
                dfs(i + 1, new_r, new_c)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    dfs(0, r, c)

        return                                 
            

