class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        # Pre-order traversal is easier for recursion
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        
        def build_tree():
            if self.i >= len(vals) or vals[self.i] == 'N':
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = build_tree()
            node.right = build_tree()
            return node
            
        return build_tree()