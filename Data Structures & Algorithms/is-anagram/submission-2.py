class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)    
        freqT = Counter(t)

        if not freqS.keys() == freqT.keys():
            return False

        for char in freqS.keys():
            if freqS[char] != freqT[char]:
                return False

        return True              