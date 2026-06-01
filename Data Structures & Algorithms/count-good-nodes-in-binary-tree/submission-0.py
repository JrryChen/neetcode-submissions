# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1 # root is always a good node
        def good_nodes(node, max_seen):
            if not node:
                return 0    
            res = 0
            if node.val >= max_seen:
                res += 1
                max_seen = node.val
            return res + good_nodes(node.left, max_seen) + good_nodes(node.right, max_seen)
        return good_nodes(root, root.val)              