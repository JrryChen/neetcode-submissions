class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def backtrack(opened, closed):
            if opened == closed == n:
                # found valid parentheses
                res.append(''.join(curr))
                return
            if opened < n:
                curr.append('(')
                backtrack(opened + 1, closed)
                curr.pop()
            if closed < opened:
                curr.append(')')
                backtrack(opened, closed + 1)
                curr.pop()
        backtrack(0, 0)
        return res        


