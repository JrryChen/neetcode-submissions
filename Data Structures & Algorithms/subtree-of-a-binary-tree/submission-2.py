# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True

        def compare(n1, n2):
            # Checks to see if trees are the same
            if not n1 and not n2:
                return True
            if not n1:
                return False
            if not n2:
                return False
            if n1.val == n2.val:
                return compare(n1.left, n2.left) and compare(n1.right, n2.right) 
            return False

        if compare(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)        
