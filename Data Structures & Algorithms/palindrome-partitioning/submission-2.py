class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []
        part = []
        def bt(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if palindrome(i, j):
                    part.append(s[i:j + 1])
                    bt(j + 1)
                    part.pop()

        bt(0)
        return res                        
        