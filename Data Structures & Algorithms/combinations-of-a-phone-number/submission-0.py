class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keypad = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        res = []
        def dfs(curr, i):
            if i >= len(digits):
                res.append(''.join(curr))
                return
            for c in keypad[digits[i]]:
                curr.append(c)
                dfs(curr, i + 1)
                curr.pop()
        dfs([], 0)
        return res            