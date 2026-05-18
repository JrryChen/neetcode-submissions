class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res, l, maxf = 0, 0, 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])
            if (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res        
        