# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        if p and q are both < root, root.left is a CA
        if p and q are both > root, root.right is a CA
        if root is equal to p or q or if it is between the two, that is LCA
        '''
        if not root:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p , q)
        elif p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root