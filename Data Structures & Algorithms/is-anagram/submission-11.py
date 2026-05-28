class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        for char_s in s:
            freq_s[char_s] = 1 + freq_s.get(char_s, 0)
        for char_t in t:
            freq_t[char_t] = 1 + freq_t.get(char_t, 0) 
        return freq_t == freq_s       