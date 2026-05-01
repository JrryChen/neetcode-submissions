# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        bfs until we find a node = to subRoot
        bfs comopare
        '''
        def dfsCompare(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return dfsCompare(node1.left, node2.left) and dfsCompare(node1.right, node2.right)
            return False
            
        if not subRoot:
            return True
        if not root:
            return False

        if dfsCompare(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)          

            

