class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_word = True

    def search(self, word):
        current = self 
        for c in word:
            if c not in current.children:
                return False
            
            current = current.children[c]
        return current.is_word


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = TrieNode()

        for w in wordDict:
            trie.add(w)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break

        return dp[n]
        