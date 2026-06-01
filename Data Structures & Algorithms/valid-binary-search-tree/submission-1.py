class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False  
            # child nodes are valid so check their children
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)  
        return dfs(root, float('-inf'), float('inf'))