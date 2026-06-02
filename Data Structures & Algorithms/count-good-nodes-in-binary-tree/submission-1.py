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

        def count(node, max_seen):
            if not node:
                return 0
            self = 0   
            if node.val >= max_seen:
                max_seen = node.val
                self = 1
            left, right = 0, 0
            if node.left:
                left = count(node.left, max_seen)
            if node.right:
                right = count(node.right, max_seen)
            return self + left + right  

        return count(root, root.val)