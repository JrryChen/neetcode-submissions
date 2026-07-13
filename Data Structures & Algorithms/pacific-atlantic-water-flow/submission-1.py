class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        for each cell, dfs if it can reach pacific and dfs if it can reach atlantic
        '''
        m, n = len(heights), len(heights[0])
        output = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def pacific(r, c, visited):
            if r == 0 or c == 0:
                return True  
            visited.add((r, c))
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy
                if not(0 <= new_r < m) or not(0 <= new_c < n) or (new_r, new_c) in visited:
                    continue
                if heights[r][c] >= heights[new_r][new_c]:
                    if pacific(new_r, new_c, visited):
                        return True
            return False                

        def atlantic(r, c, visited):
            if r == m - 1 or c == n - 1:
                return True
            visited.add((r, c))
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy
                if not(0 <= new_r < m) or not(0 <= new_c < n) or (new_r, new_c) in visited:
                    continue
                if heights[r][c] >= heights[new_r][new_c]:
                    if atlantic(new_r, new_c, visited):
                        return True
            return False  

        for r in range(m):
            for c in range(n):
                if pacific(r, c, set()) and atlantic(r, c, set()):
                    output.append([r, c])
        return output