class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start with the widest possible range
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node, low, high):
        if not node:
            return True

        # Now the root will pass: -inf < root.val < inf is always True
        if not (low < node.val < high):
            return False

        return self.validate(node.left, low, node.val) and \
               self.validate(node.right, node.val, high)