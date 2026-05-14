class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + '#' + s
        return res    
    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            res.append(s[right + 1: right + length + 1])
            left = right + length + 1
        return res        