class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True       
        
    def search(self, word: str) -> bool:
        def dfs(root, word):
            curr = root
            for i in range(len(word)):
                c = word[i]
                if c == '.':
                    for c_key in curr.children.keys():
                        if dfs(curr.children[c_key], word[i+1:]):
                            return True
                    return False             
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.word 
        return dfs(self.root, word)           

