class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in seen: # we need while we need t move l left until we get a s[l] that is not s[r]
                seen.remove(s[l])
                l += 1
            seen.add(s[r])    
            res = max(res, r - l + 1)
        return res        
                