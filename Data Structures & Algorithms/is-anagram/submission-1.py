class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = Counter(s)
        freqT = Counter(t)
        if not freqS.keys() == freqT.keys():
            return False
        for key in freqS.keys():
            if freqS[key] != freqT[key]:
                return False
        return True        