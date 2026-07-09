"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        maintain a hash set to map nodes to already created nodes

        dfs
            if its already in the hashset, we return the cloned node
            if not, we clone it
        '''
        node_map = {}
        if not node:
            return None

        def dfs(node):
            if node in node_map:
                return node_map[node]
            clone = Node(node.val)
            node_map[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone    

        return dfs(node)            
