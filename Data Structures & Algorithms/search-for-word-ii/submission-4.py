class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        optimized approach
        make a prefix tree of words to help prune out paths of dfs that isn't feasible
        
        '''

        if not board:
            return []
        if not words:
            return []
        
        # Build prefix tree for words
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children: 
                    curr.children[c] = TrieNode() 
                curr = curr.children[c] 
            curr.word = True
        res = set()
        directions = [
            (1, 0), # right
            (0, 1), # up
            (-1, 0), # left
            (0, -1) # down
        ]
        # dfs
        def dfs(builder, row, col, node, seen):
            seen.add((row, col))
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if not (0 <= new_row < len(board)) or not (0 <= new_col < len(board[0])):
                    # new coords are out of bounds
                    continue
                if (new_row, new_col) in seen:
                    continue       
                c = board[new_row][new_col]    
                if c not in node.children:
                    # this path has no possible words
                    continue    
                next_node = node.children[c]
                # check if the added char would make a word
                if next_node.word:
                    res.add(builder + c)
                # step through    
                dfs(builder + c, new_row, new_col, next_node, seen)
                seen.remove((new_row, new_col))    

        # start from each character in grid
        for r in range(len(board)):
            for c in range(len(board[r])):
                ch = board[r][c]
                if ch not in root.children:
                    continue
                curr = root.children[ch]
                if curr.word:
                    res.add(ch)
                seen = set() # list of coords visited        
                dfs(ch, r, c, curr, seen)

        return list(res)          

