# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = float('-inf')
        def dfs(node):
            if not node: return 0
            nonlocal res
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(res, node.val + left + right)
            return max(node.val, node.val + max(left, right))
        dfs(root)
        return res    