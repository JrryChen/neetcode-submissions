class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        make words in to a trie so we can prune out paths that won't lead to words
        then dfs each coordinate maintaining a hashset to avoid revisiting cells 
            and res is a set to avoid refinding words
        '''
        # Create Trie
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True
        
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0), 
            (0, -1)
        ]
        def dfs(builder, r, c, seen, curr):
            if curr.word:
                res.add(builder)
            for dx, dy in directions:
                new_r, new_c = r + dx, c + dy
                if not (0 <= new_r < len(board)) or not (0 <= new_c < len(board[0])):
                    # Index out of bounds
                    continue
                if (new_r, new_c) in seen:
                    # visited this cell already so skip
                    continue 
                ch = board[new_r][new_c]
                if ch not in curr.children:
                    # doesn't lead to a word
                    continue
                seen.add((new_r, new_c))    
                dfs(builder + ch, new_r, new_c, seen, curr.children[ch])
                seen.remove((new_r, new_c))
                   

        res = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                ch = board[r][c]
                if ch not in root.children:
                    continue
                curr = root.children[ch]    
                seen = {(r, c)}
                dfs(ch, r, c, seen, curr)
        return list(res)            

