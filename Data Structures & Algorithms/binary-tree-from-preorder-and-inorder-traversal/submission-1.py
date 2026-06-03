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

        # first node in preorder is the root
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # the left subtree of root is all nodes to left of mid in inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) 
        # right subtree of root is all nodes right of mid inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root