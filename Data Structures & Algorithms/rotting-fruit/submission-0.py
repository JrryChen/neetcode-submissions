class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        time = 0
        fresh = 0
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1: 
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    new_r, new_c = r + dx, c + dy
                    if not (0 <= new_r < m) or not (0 <= new_c < n):
                        continue
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append([new_r, new_c]) 
            time += 1
        return -1 if fresh else time     