# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # search each node and see if p and q are in it
        # curr = root

        # while curr:
        #     if p.val > curr.val and q.val > curr.val:
        #         # search right
        #         curr = curr.right
            
        #     elif p.val < curr.val and q.val < curr.val:
        #         # search left 
        #         curr =curr.left
            
        #     else: 
        #         return curr






        # doing it using post order

        if root is None or root.val ==p.val or root.val ==q.val:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root

        return left if left else right






