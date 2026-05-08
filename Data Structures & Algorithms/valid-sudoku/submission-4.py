class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        have a dict of sets containing seen numbers in either a row, col or square
        for each coord, check if it is valid
        '''

        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in row[r]:
                    return False
                elif val in col[c]:
                    return False
                elif val in square[(r // 3, c // 3)]:
                    return False
                else:
                    row[r].add(val)
                    col[c].add(val)
                    square[(r // 3, c // 3)].add(val)

        return True                     