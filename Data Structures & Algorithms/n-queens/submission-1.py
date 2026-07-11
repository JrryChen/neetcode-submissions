class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr = []

        def valid(r, c):
            if r == 0:
                return True

            # vertical check
            for i in range(len(curr)):
                if curr[i][c] == 'Q': return False
            
            # diagonal check
            curr_r, c_offset = r - 2, 1
            while curr_r >= 0:
                left, right = c - c_offset, c + c_offset
                if 0 <= left < n:
                    if curr[curr_r][left] == 'Q': return False
                if 0 <= right < n:
                    if curr[curr_r][right] == 'Q': return False
                curr_r -= 1
                c_offset += 1
            return True            
          
        def dfs(r):
            if r >= n:
                to_add = []
                for row in curr:
                    to_add.append(''.join(row))
                res.append(to_add)
                return
            for c in range(n):
                if valid(r + 1, c): # if the next row and col spot is valid
                    to_add = ['.'] * n
                    to_add[c] = 'Q'
                    curr.append(to_add)
                    dfs(r + 1)
                    curr.pop()

        dfs(0)
        return res            