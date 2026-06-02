# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # first value in preorder is always root
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # second value in preorder is alwasy root.left
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) # pass in the left tree preorder and inorder arrays
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1: ])
        return root