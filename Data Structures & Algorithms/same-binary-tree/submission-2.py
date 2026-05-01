# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        recursive dfsCompare(n1, n2):
            if not n1 and n2 or n1 and not n2:
                return False

            if n1.val is not n2.val:
                return False

            if not n1.left and not n2.left and not n1.right and not n2.right: # Both nodes are a leaf
                return True
            elif (not n1.left and n2.left) or (n1.left and not n2.left): #one node doesn't have a left
                return False
            elif same for right
            else: #both nodes have left and right

                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)            
        '''

        def dfsCompare(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 and n2 or n1 and not n2:
                return False

            if n1.val is not n2.val:
                return False

            if not n1.left and not n2.left and not n1.right and not n2.right: # Both nodes are a leaf
                return True
            elif (not n1.left and n2.left) or (n1.left and not n2.left): #one node doesn't have a left
                return False
            elif (not n1.right and n2.right) or (n1.right and not n2.right):
                return False
            else: #both nodes have left and right
                return dfsCompare(n1.left, n2.left) and dfsCompare(n1.right, n2.right)

        return dfsCompare(p, q)        
        
        