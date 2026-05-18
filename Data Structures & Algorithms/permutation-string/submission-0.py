class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        freq = [0] * 26

        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            freq[ord(s2[r]) - ord('a')] += 1
            if sum(freq) < len(s1):
                continue
            if s1_freq == freq:
                return True
            freq[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False           