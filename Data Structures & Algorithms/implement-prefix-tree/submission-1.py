class TreeNode:
    def __init__(self):
        self.children = {} # dictionary of children ('char' : Node)
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.is_end = True    

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # if curr.children is not empty, it is not a word so return False
        return curr.is_end # if curr.children is not empty, it is not a word so return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        