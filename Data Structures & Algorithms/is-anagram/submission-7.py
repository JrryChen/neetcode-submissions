class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        if s_count.keys() != t_count.keys():
            return False

        for key in s_count.keys():
            if s_count[key] != t_count[key]:
                return False
        return True            