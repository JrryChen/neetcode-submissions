class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        res = []
        curr = []

        def valid(r, c):
            # we are on first row
            if not curr: return True

            # col check
            for i in range(len(curr)):
                if curr[i][c] == 'Q':
                    return False

            # left up diagonal check (-1, -1)
            curr_r, dc = r - 2, 1
            while 0 <= curr_r < len(curr):
                left, right = c - dc, c + dc
                if 0 <= left < n:
                    if curr[curr_r][left] == 'Q':
                        return False
                if 0 <= right < n:
                    if curr[curr_r][right] == 'Q':
                        return False
                curr_r -= 1
                dc += 1

            return True                    

                   

        def dfs(r):
            if r >= n:
                to_add = []
                for row in curr:
                    to_add.append(''.join(row))
                res.append(to_add)
                return
            for c in range(n):
                if valid(r+1, c):
                    curr_to_add = ['.'] * n
                    curr_to_add[c] = 'Q'
                    curr.append(curr_to_add)
                    dfs(r + 1)
                    curr.pop()

        dfs(0)
        return res                               