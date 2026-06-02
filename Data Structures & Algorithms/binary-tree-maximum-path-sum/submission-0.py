# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        dfs down to leaf node
        if leaf node:
            we take the root value
        compare root value to root value + left + right children, thats the max possible at that node
        we send back either root value or rootvalue + max(left, right)    
        '''
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = max(dfs(node.left), 0) #if children are negative values, better to not use them in the path
            right = max(dfs(node.right), 0)
            res = max(res, max(node.val, node.val + left + right))
            return max(node.val, node.val + max(left, right))
        dfs(root)
        return res    

                