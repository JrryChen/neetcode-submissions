class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        n = len(res)

        for i in range(1, len(strs)):
            for j in range(n):
                string = list(strs[i])
                if j >= len(string) or res[j] != string[j]:
                    n = j
                    break

        return res[:n]           